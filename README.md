# Python Ogreniyorum

Python ogrenme surecimde gelistirdigim projeler ve alistirmalarin bulundugu repodur.

## Projeler

### Not Defteri
`phyton-ogreniyorum/notdefteri/notDefteri.py`

Dosya tabanli basit bir not defteri uygulamasi.

- Not ekleme
- Notlari goruntuleme
- Notlari temizleme
- Konsol menu arayuzu

### Ogrenci Bilgi Sistemi
`phyton-ogreniyorum/ogrenci-bilgi-sistemi/ogrenci.py`

OOP prensiplerine gore yazilmis ogrenci yonetim sistemi.

- Ogrenci ekleme / silme / guncelleme
- Not girisi (0-100)
- Okul ortalamasi hesaplama
- `Ogrenci` sinifi ile nesne tabanli tasarim

### IMDB Top 100
`phyton-ogreniyorum/IMDB-TOP-100/ImdbTop100.py`

IMDb'den web scraping ile ilk 100 filmin bilgilerini ceken program.

- `requests` ve `BeautifulSoup` kullanimi
- JSON parse etme
- Film adi, yil, yonetmen ve basrol oyuncularini listeleme

### HTTP/HTTPS Proxy Sunucusu
`phyton-ogreniyorum/proxy/proxy.py`

Tam ozellikli, cok is parcacikli bir HTTP/HTTPS proxy sunucusu.

- HTTP ve HTTPS (CONNECT tuneli) destegi
- `ThreadPoolExecutor` ile eszamanli baglanti yonetimi
- Baglanti istatistikleri (toplam baglanti, transfer edilen byte vb.)
- Graceful shutdown (SIGINT / SIGTERM)
- CLI argumanlari: `--host`, `--port`, `--workers`, `--log-level`

**Kullanim:**
```bash
python proxy.py
python proxy.py --host 0.0.0.0 --port 8080 --workers 50 --log-level DEBUG
```

### Sakalar
`phyton-ogreniyorum/pip/sakalar.py`

`pyjokes` kutuphanesi kullanilarak rastgele saka yazdiran kisa bir program.

## Kullanilan Teknolojiler

- Python 3
- `requests`
- `BeautifulSoup4`
- `pyjokes`
- Standart kutuphane: `socket`, `threading`, `argparse`, `logging`, `json`

## Kurulum

```bash
pip install requests beautifulsoup4 pyjokes
```
