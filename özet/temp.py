# -*- coding: utf-8 -*-
"""
PYTHON ÖZET VE TEKRAR DOSYASI
Bu dosya ihtiyaç duyulduğunda Python konularını tekrar etmek için hazırlanmıştır.
İçerisindeki kodlar bölümlere ayrılmış olup, hepsi okunabilir şekilde düzenlenmiştir.
"""

# ==========================================
# 1. TEMEL İŞLEMLER (PRINT, FORMAT, INPUT)
# ==========================================

print("hello world!")
# Noktalı virgül kullanılmak zorunda değil
print("merhaba {}".format("dünya"))
# Modern format kullanımı (f-string)
print(f"merhaba {'ben'}")

hız = 70
print(f"Lütfen yavaş, hızınız = {hız}")
print("Lütfen yavaş, hızınız", hız)
print("\n")

# Değişken Atama ve Kullanımı
otomobil_hız = 90
otomobil_marka = "opel"
otomobil_km = 520.2 * 2

print(f"Araç belirlendi: Hızı {otomobil_hız}, Markası {otomobil_marka}, KM'si {otomobil_km} \n")

# Input (Kullanıcıdan Veri Alma)
# print("merhaba " + input("İsminizi girin: "))
# otomobil_hız = input("Otomobil hızını giriniz: ")

# ==========================================
# 2. VERİ TİPLERİ, DÖNÜŞÜMLER VE STRİNG METOTLARI
# ==========================================

# Uzunluk (len)
a = len("selam")
print("Uzunluk:", a)

# Sayısal İşlemler
x = 4.5000000000001
print("Yuvarlama:", round(x))

# String Metotları (YENİ EKLENDİ)
metin = "Python Öğreniyorum"
print("Küçük Harf:", metin.lower())    # python öğreniyorum
print("Büyük Harf:", metin.upper())    # PYTHON ÖĞRENİYORUM
print("Bölme (Split):", metin.split(" ")) # ['Python', 'Öğreniyorum']
print("Değiştirme (Replace):", metin.replace("Python", "Yazılım")) 

# ==========================================
# 3. HATA YAKALAMA (TRY - EXCEPT - FINALLY)
# ==========================================

try:
    # x = int(input("Lütfen bir tam sayı giriniz: "))
    x = 21 # Sabit değer (Test için)
    if x > 20 and x % 2 == 1:
        print("Girdiğiniz sayı 20'den büyük veya tek bir sayı.")
    else:
        print("Lütfen 20'den büyük veya tek bir sayı giriniz.")
except ValueError:
    print("❌ Hata: Lütfen sadece bir tam sayı girin.")
except Exception as e: # (YENİ EKLENDİ) Diğer tüm hataları yakalamak için
    print(f"Beklenmedik bir hata oluştu: {e}")
finally: # (YENİ EKLENDİ) Hata olsa da olmasa da çalışır
    print("Hata kontrol bloğu tamamlandı.\n")

# ==========================================
# 4. DÖNGÜLER (FOR, WHILE)
# ==========================================

# FOR Döngüsü
baslangic, bitis = 1, 10
toplam = 0

print("Tek sayılar:" )
for sayi in range(baslangic, bitis+1):
    if sayi % 2 != 0:
        print(sayi, end=" ")
    toplam += sayi

print(f"\n{baslangic}'dan {bitis}'e kadar sayıların toplamı {toplam}'dir\n")

# WHILE Döngüsü ile Hesap Makinesi Örneği
# (Örnek duraklamaması için yorum satırında bırakıldı)
"""
while True:
    print("1-Toplama, 2-Çıkarma, 3-Çarpma, 4-Bölme, 0-Çıkış")
    secim = int(input("Bir işlem seçiniz: "))
    if secim == 0: break
    a = float(input("1. sayıyı giriniz: "))
    b = float(input("2. sayıyı giriniz: "))
    if secim == 1: print("Sonuç: ", a + b)
    elif secim == 4 and b != 0: print("Sonuç: ", a / b)
"""

# ==========================================
# 5. LİSTE ÜRETEÇLERİ (LIST COMPREHENSION)
# ==========================================

# Klasik Yöntem
kareler = []
for x in range(1,11):
    kareler.append(x**2)
print(f"Klasik Döngü Sayılar: {kareler}")

# Çok daha basit ve hızlı gösterimi (List Comprehension)
kareler_comp = [x**2 for x in range(1,11)]
print(f"List Comprehension: {kareler_comp}\n")

# ==========================================
# 6. VERİ YAPILARI (LIST, TUPLE, SET, DICT)
# ==========================================

# [] => List, () => Tuple, {} => Set, {key:value} => Dictionary

# LIST (Değiştirilebilir - Mutable)
isimler = ["ali", "ece", "merve", "semih"]
numaralar = [131, 423, 231, 463]
yeni_dizi = []

# Zip Fonksiyonu (İki listeyi eşleştirir)
for isim, numara in zip(isimler, numaralar):
    yeni_dizi.append(isim + " " + str(numara))
print("Zip Kullanımı:", yeni_dizi)

# Enumerate Fonksiyonu (YENİ EKLENDİ)
print("Öğrenci Listesi:")
for index, isim in enumerate(isimler):
    print(f"{index + 1}. Öğrenci: {isim}")

# TUPLE (Değiştirilemez - Immutable)
derslerTuple = ("fizik", "ingilizce", "matematik")
# derslerTuple[0] = "kimya" # TypeError verir!

# SET (Sırasız - Eşsiz elemanlar tutar)
derslerSet = {"Tarih", "Matematik", "Fizik"}
derslerSet.add("Kimya")
print("\nSet İçinde Arama ('Fizik' var mı?):", "Fizik" in derslerSet)

sanatDersleriSet = {"Tarih", "Piyano"}
print("Kesişim:", derslerSet.intersection(sanatDersleriSet))
print("Fark:", derslerSet.difference(sanatDersleriSet))

# DICTIONARY (Sözlük - Anahtar:Değer)
ogrencilerDict = {100: "Ali Kaya", 102: "Ali Korkmaz"}
# get() metodu, anahtar yoksa hata vermez
print("Sözlük Elemanı:", ogrencilerDict.get(100, "Bulunamadı")) 
print("\n")

# ==========================================
# 7. FONKSİYONLAR (*ARGS, **KWARGS, SCOPE)
# ==========================================

# Kapsam (Scope)
x_val = 10 # Global değişken
def ornek_global():
    global x_val
    x_val *= 2
    print("Global x:", x_val)

ornek_global()

# Varsayılan Parametre
def selamla(isim="Misafir"):
    print("Merhaba", isim)

selamla()

# Belirsiz Sayıda Parametre Almak (*args)
def toplam_args(*args):
    return sum(args)
print("Args Toplam:", toplam_args(1, 2, 3, 4, 5))

# İsimlendirilmiş Belirsiz Parametre (**kwargs)
def kisiBilgileri(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

kisiBilgileri(ad="Semih", yas=25, sehir="Malatya")

# SAYI TAHMİN OYUNU
def sayi_tahmin_oyunu():
    import random
    hak = 3
    sayi = random.randint(1, 10)
    print(f"\n[Oyun Başladı] 1-10 arası sayı tutuldu. {hak} hakkınız var.")
    while hak > 0:
        tahmin = input("Tahmininiz: ")
        if not tahmin.isdigit(): continue
        tahmin = int(tahmin)
        if tahmin < sayi: print("Büyük.")
        elif tahmin > sayi: print("Küçük.")
        else: 
            print("Bildiniz!") 
            break
        hak -= 1
# sayi_tahmin_oyunu() # Çalıştırmak için yorumdan çıkarın

# ==========================================
# 8. İLERİ DÜZEY FONKSİYONLAR (LAMBDA, MAP, FILTER) (YENİ EKLENDİ)
# ==========================================

# Lambda Fonksiyonu (Tek satırlık isimsiz fonksiyonlar)
kare_al = lambda x: x ** 2
print("\nLambda ile kare alma:", kare_al(5))

# Map (Bir fonksiyonu listenin tüm elemanlarına uygular)
sayilar = [1, 2, 3, 4, 5]
kareler_map = list(map(lambda x: x**2, sayilar))
print("Map kullanımı:", kareler_map)

# Filter (Belirli bir koşulu sağlayanları filtreler)
cift_sayilar = list(filter(lambda x: x % 2 == 0, sayilar))
print("Filter kullanımı:", cift_sayilar)

# ==========================================
# 9. MODÜLLER (RANDOM, DATETIME)
# ==========================================

import random
print("\nRastgele Sayı:", random.randint(1, 100))
isimler_kopya = isimler.copy()
random.shuffle(isimler_kopya)
print("Karıştırılmış Liste:", isimler_kopya)

import datetime # (YENİ EKLENDİ)
suan = datetime.datetime.now()
print("Şu Anki Zaman:", suan)
print(f"Yıl: {suan.year}, Ay: {suan.month}, Gün: {suan.day}\n")

# ==========================================
# 10. NESNE YÖNELİMLİ PROGRAMLAMA (OOP)
# ==========================================

class Tesla:   
    tesla_count = 0  # Sınıf değişkeni
    gecerli_renkler = ["Beyaz", "Siyah"]
    
    def __init__(self, renk="Beyaz", batarya="Uzun", otopilot=False):
        # Encapsulation (Gizli değişkenler __degisken)
        self.__renk = renk if renk in Tesla.gecerli_renkler else "Beyaz"
        self.__batarya = batarya
        self.__otopilot = otopilot
        self.__hiz = 0
        Tesla.tesla_count += 1
       
    def goster_bilgi(self):
        print(f"Renk: {self.__renk}, Batarya: {self.__batarya}, Hız: {self.__hiz}")

    def hizlan(self, miktar):
        self.__hiz += miktar

benim_teslam = Tesla(renk="Siyah")
benim_teslam.hizlan(70)
benim_teslam.goster_bilgi()

# INHERITANCE (KALITIM) VE POLYMORPHISM
class Hayvan:
    def __init__(self, isim):
        self.isim = isim
    def ses_cikar(self):
        print("Hayvan ses çıkarıyor")

class Kedi(Hayvan): 
    # Override (Ezme)
    def ses_cikar(self):
        print(f"{self.isim} miyavlıyor")

kedi1 = Kedi("Mercan")
kedi1.ses_cikar()

# ==========================================
# 11. DECORATORS VE GENERATORS (YENİ EKLENDİ)
# ==========================================

# DECORATOR (Fonksiyonun çalışma şeklini değiştiren yapılar)
def zaman_olcer(fonksiyon):
    import time
    def wrapper(*args, **kwargs):
        baslangic = time.time()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.time()
        print(f"{fonksiyon.__name__} {bitis - baslangic:.4f} saniye sürdü.")
        return sonuc
    return wrapper

@zaman_olcer
def test_fonksiyonu():
    import time
    time.sleep(0.5)

test_fonksiyonu()

# GENERATOR (Belleği yormadan eleman üreten yapılar - yield)
def sayi_ureteci(max_deger):
    sayac = 1
    while sayac <= max_deger:
        yield sayac
        sayac += 1

gen = sayi_ureteci(3)
print("\nGenerator Değerleri:", next(gen), next(gen), next(gen))

# ==========================================
# 12. DOSYA İŞLEMLERİ (TEXT VE JSON)
# ==========================================

import json

# 'w' -> Yazma, 'r' -> Okuma, 'a' -> Ekleme (YENİ EKLENDİ)
data_dict = {"kişiler": [{"ad": "Ahmet", "yas": 30}]}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data_dict, file, ensure_ascii=False, indent=4)

with open("data.json", "r", encoding="utf-8") as file:
    okunan = json.load(file)
    print("\nJSON'dan okunan ad:", okunan["kişiler"][0]["ad"])

# Normal Metin (Text) Dosyası Yazma ve Okuma (YENİ EKLENDİ)
with open("notlar.txt", "w", encoding="utf-8") as file:
    file.write("Dosya işlemleri başarıyla tamamlandı.\n")

with open("notlar.txt", "r", encoding="utf-8") as file:
    print("Text Dosyası İçeriği:", file.read())

print("\n--- TEKRAR DOSYASI BAŞARIYLA ÇALIŞTIRILDI ---")