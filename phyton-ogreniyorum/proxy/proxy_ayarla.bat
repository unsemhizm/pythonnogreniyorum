@echo off
echo Proxy ayarlari yapiliyor...
netsh winhttp set proxy proxy-server="127.0.0.1:8888" bypass-list="localhost;127.*;10.*;172.16.*;172.17.*;172.18.*;172.19.*;172.20.*;172.21.*;172.22.*;172.23.*;172.24.*;172.25.*;172.26.*;172.27.*;172.28.*;172.29.*;172.30.*;172.31.*;192.168.*"
echo.
echo Proxy ayari basariyla yapildi!
echo Proxy: 127.0.0.1:8888
echo.
echo Proxy'yi kapatmak icin proxy_kapat.bat dosyasini calistirin.
pause

