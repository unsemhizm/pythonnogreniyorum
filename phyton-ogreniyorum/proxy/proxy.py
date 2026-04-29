#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTTP/HTTPS Proxy Server
Kullanim: python proxy.py [--host HOST] [--port PORT] [--workers N] [--log-level LEVEL]
"""

import argparse
import logging
import select
import signal
import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from typing import Optional, Tuple

# ---------------------------------------------------------------------------
# Sabitler
# ---------------------------------------------------------------------------
BUFFER_SIZE = 8192
TIMEOUT = 15
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8888
DEFAULT_WORKERS = 100

# ---------------------------------------------------------------------------
# Loglama
# ---------------------------------------------------------------------------
LOG_FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging(level: str = "INFO") -> logging.Logger:
    logging.basicConfig(format=LOG_FORMAT, datefmt=DATE_FORMAT, level=level.upper())
    return logging.getLogger("proxy")


logger = logging.getLogger("proxy")


# ---------------------------------------------------------------------------
# Istatistikler
# ---------------------------------------------------------------------------
@dataclass
class Stats:
    total_connections: int = 0
    active_connections: int = 0
    http_requests: int = 0
    https_requests: int = 0
    errors: int = 0
    bytes_transferred: int = 0
    _lock: threading.Lock = field(default_factory=threading.Lock)

    def connection_start(self) -> None:
        with self._lock:
            self.total_connections += 1
            self.active_connections += 1

    def connection_end(self) -> None:
        with self._lock:
            self.active_connections = max(0, self.active_connections - 1)

    def record_http(self) -> None:
        with self._lock:
            self.http_requests += 1

    def record_https(self) -> None:
        with self._lock:
            self.https_requests += 1

    def record_error(self) -> None:
        with self._lock:
            self.errors += 1

    def add_bytes(self, n: int) -> None:
        with self._lock:
            self.bytes_transferred += n

    def report(self) -> str:
        with self._lock:
            return (
                f"Toplam baglanti: {self.total_connections} | "
                f"Aktif: {self.active_connections} | "
                f"HTTP: {self.http_requests} | "
                f"HTTPS: {self.https_requests} | "
                f"Hata: {self.errors} | "
                f"Transfer: {self.bytes_transferred / 1024:.1f} KB"
            )


# ---------------------------------------------------------------------------
# Proxy Sunucusu
# ---------------------------------------------------------------------------
class ProxyServer:
    def __init__(
        self,
        host: str = DEFAULT_HOST,
        port: int = DEFAULT_PORT,
        max_workers: int = DEFAULT_WORKERS,
    ) -> None:
        self.host = host
        self.port = port
        self.max_workers = max_workers
        self.server_socket: Optional[socket.socket] = None
        self.running = False
        self.stats = Stats()
        self._executor: Optional[ThreadPoolExecutor] = None

    # ------------------------------------------------------------------
    # Baslatma / Durdurma
    # ------------------------------------------------------------------
    def start(self) -> None:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.settimeout(1.0)  # accept() icin kisa timeout (signal icin)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(200)
        self.running = True

        self._executor = ThreadPoolExecutor(
            max_workers=self.max_workers, thread_name_prefix="proxy-worker"
        )

        logger.info("Proxy baslatildi -> %s:%d (max_workers=%d)", self.host, self.port, self.max_workers)

        try:
            while self.running:
                try:
                    client_socket, addr = self.server_socket.accept()
                    client_socket.settimeout(TIMEOUT)
                    self._executor.submit(self._handle_client, client_socket, addr)
                except socket.timeout:
                    continue  # accept timeout -> sinyal kontrolu icin donguye devam
                except OSError:
                    if self.running:
                        raise
        finally:
            self.stop()

    def stop(self) -> None:
        if not self.running:
            return
        self.running = False
        logger.info("Proxy durduruluyor...")

        if self._executor:
            self._executor.shutdown(wait=False)
        if self.server_socket:
            try:
                self.server_socket.close()
            except OSError:
                pass

        logger.info("Proxy durduruldu.")
        logger.info(self.stats.report())

    # ------------------------------------------------------------------
    # Istemci isleme
    # ------------------------------------------------------------------
    def _handle_client(self, client_socket: socket.socket, addr: Tuple[str, int]) -> None:
        self.stats.connection_start()
        try:
            request = self._recv_request(client_socket)
            if not request:
                return

            first_line = request.split(b"\r\n")[0]
            method = first_line.split(b" ")[0].upper()

            if method == b"CONNECT":
                self.stats.record_https()
                self._handle_https(client_socket, request, addr)
            else:
                self.stats.record_http()
                self._handle_http(client_socket, request, addr)

        except Exception as exc:
            self.stats.record_error()
            logger.debug("Istemci hatasi %s: %s", addr, exc)
        finally:
            self.stats.connection_end()
            _close_socket(client_socket)

    # ------------------------------------------------------------------
    # HTTP
    # ------------------------------------------------------------------
    def _handle_http(
        self,
        client_socket: socket.socket,
        request: bytes,
        addr: Tuple[str, int],
    ) -> None:
        request = _strip_proxy_headers(request)
        host, port = _parse_host_header(request)
        if not host:
            logger.warning("HTTP: Host baslik bulunamadi (%s)", addr)
            return

        logger.info("HTTP  %s:%d <- %s", host, port, addr[0])

        target = _connect_target(host, port)
        if target is None:
            self.stats.record_error()
            return

        try:
            target.sendall(request)
            transferred = self._relay(client_socket, target)
            self.stats.add_bytes(transferred)
        finally:
            _close_socket(target)

    # ------------------------------------------------------------------
    # HTTPS (CONNECT tuneli)
    # ------------------------------------------------------------------
    def _handle_https(
        self,
        client_socket: socket.socket,
        request: bytes,
        addr: Tuple[str, int],
    ) -> None:
        first_line = request.split(b"\r\n")[0]
        parts = first_line.split(b" ")
        if len(parts) < 2 or b":" not in parts[1]:
            logger.warning("HTTPS: Gecersiz CONNECT istegi (%s)", addr)
            return

        host_port = parts[1]
        host, _, raw_port = host_port.partition(b":")
        port = int(raw_port) if raw_port else 443

        logger.info("HTTPS %s:%d <- %s", host.decode(errors="replace"), port, addr[0])

        target = _connect_target(host.decode(errors="replace"), port)
        if target is None:
            self.stats.record_error()
            client_socket.sendall(b"HTTP/1.1 502 Bad Gateway\r\n\r\n")
            return

        try:
            client_socket.sendall(b"HTTP/1.1 200 Connection Established\r\n\r\n")
            transferred = self._tunnel(client_socket, target)
            self.stats.add_bytes(transferred)
        finally:
            _close_socket(target)

    # ------------------------------------------------------------------
    # Veri aktarimi
    # ------------------------------------------------------------------
    def _recv_request(self, sock: socket.socket) -> bytes:
        """HTTP istek basligini oku (header tamam olana kadar)."""
        data = b""
        try:
            while True:
                chunk = sock.recv(BUFFER_SIZE)
                if not chunk:
                    break
                data += chunk
                if b"\r\n\r\n" in data or len(chunk) < BUFFER_SIZE:
                    break
        except socket.timeout:
            pass
        return data

    def _relay(self, client: socket.socket, target: socket.socket) -> int:
        """Hedeften istemciye tek yonlu veri aktar; aktarilan byte sayisini dondur."""
        total = 0
        try:
            while True:
                data = target.recv(BUFFER_SIZE)
                if not data:
                    break
                client.sendall(data)
                total += len(data)
        except OSError:
            pass
        return total

    def _tunnel(self, sock1: socket.socket, sock2: socket.socket) -> int:
        """Iki soket arasinda cift yonlu veri tuneli; aktarilan toplam byte'i dondur."""
        sockets = [sock1, sock2]
        total = 0
        try:
            while True:
                readable, _, _ = select.select(sockets, [], [], TIMEOUT)
                if not readable:
                    break
                for s in readable:
                    try:
                        data = s.recv(BUFFER_SIZE)
                        if not data:
                            return total
                        peer = sock2 if s is sock1 else sock1
                        peer.sendall(data)
                        total += len(data)
                    except OSError as exc:
                        logger.debug("Tunnel soket hatasi: %s", exc)
                        return total
        except OSError as exc:
            logger.debug("Tunnel hatasi: %s", exc)
        return total


# ---------------------------------------------------------------------------
# Yardimci fonksiyonlar
# ---------------------------------------------------------------------------
def _strip_proxy_headers(request: bytes) -> bytes:
    lines = request.split(b"\r\n")
    return b"\r\n".join(
        ln for ln in lines if not ln.lower().startswith(b"proxy-")
    )


def _parse_host_header(request: bytes) -> Tuple[Optional[str], int]:
    for line in request.split(b"\r\n"):
        if line.lower().startswith(b"host:"):
            value = line.split(b":", 1)[1].strip()
            if b":" in value:
                h, p = value.rsplit(b":", 1)
                return h.decode(errors="replace"), int(p)
            return value.decode(errors="replace"), 80
    return None, 80


def _connect_target(host: str, port: int) -> Optional[socket.socket]:
    try:
        sock = socket.create_connection((host, port), timeout=TIMEOUT)
        return sock
    except OSError as exc:
        logger.warning("Hedefe baglanamadi %s:%d -> %s", host, port, exc)
        return None


def _close_socket(sock: Optional[socket.socket]) -> None:
    if sock is None:
        return
    try:
        sock.shutdown(socket.SHUT_RDWR)
    except OSError:
        pass
    try:
        sock.close()
    except OSError:
        pass


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="HTTP/HTTPS Proxy Sunucusu",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--host", default=DEFAULT_HOST, help="Dinlenecek adres")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Dinlenecek port")
    parser.add_argument(
        "--workers", type=int, default=DEFAULT_WORKERS, help="Maksimum es zamanli islem"
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Log seviyesi",
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Giris noktasi
# ---------------------------------------------------------------------------
def main() -> None:
    args = parse_args()
    setup_logging(args.log_level)

    proxy = ProxyServer(host=args.host, port=args.port, max_workers=args.workers)

    # Graceful shutdown: SIGINT (Ctrl+C) ve SIGTERM
    def _shutdown(signum, _frame):  # noqa: ANN001
        logger.info("Sinyal alindi (%s), kapatiliyor...", signal.Signals(signum).name)
        proxy.stop()
        sys.exit(0)

    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    proxy.start()


if __name__ == "__main__":
    main()
