# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
print("hello world!");
#noktalı virgül kullanılmak zorunda değil
print("merhaba {}".format("dünya"));
# modern format kullanımı 
print(f"merhaba {'ben'}")
"""

"""
hız = 70
print(hız)

print(f"lutfen yavas hızınız = {hız}")
print("lütfen yavaş hıznınz ",hız)
print("\n")


otomobil_hız = 90
otomobil_marka = "opel"
otomobil_km = 520.2 * 2

print(f"arac belirlendi hızı {otomobil_hız} markası {otomobil_marka} km'si {otomobil_km} \n")

#print("merhaba" + " semih")

print("merhaba" + " " + input("isminizi girin: "))

otomobil_hız = input("otomobil hızını giriniz: ")
otomobil_km = input("otomobil km sini giriniz: ")
otomobil_marka = input("otomobil markasını giriniz: ")

print(f"aracı belirrtiniz hızı {otomobil_hız} km si {otomobil_km} markası {otomobil_marka}")


a = len("selam")
print(a)

print("İsminizin uzunluğu: " + str(len(input("İsminizi giriniz: "))))

x = 4.5000000000001
print(round(x))

not1 = float(input("1. notu giriniz: "))

not2 = float(input("2. notu giriniz: "))

not3 = float(input("3. notu giriniz: "))

toplam = not1 + not2 + not3

ortlama = float(toplam / 3);

print(f"ortalama {ortlama:.2f}")

try:
    x = int(input("Lütfen bir tam sayı giriniz: "))

    if x > 20 and x % 2 == 1:
        print("Girdiğiniz sayı 20'den büyük veya tek bir sayı.")
    else:
        print("Lütfen 20'den büyük veya tek bir sayı giriniz.")
        
except ValueError:
    print("❌ Hata: Lütfen sadece bir tam sayı girin.")





baslangic = int(input("başlangıç değerini giriniz: "))
bitis = int(input("bitis değerini giriniz: "))

toplam = 0
print("tek sayılar:" )

for sayi in range(baslangic, bitis+1):
    if sayi % 2 != 0:
        print(sayi,end=" ")
    toplam += sayi

print("")
print(f"{baslangic} dan {bitis} e kadar olan sayiların toplamı {toplam} dir")    

"""

"""
kareler = []
for x in range(1,11):
    kareler.append(x**2)

print(f"sayılar: {kareler}")

# bu for döngüsünün çok daha basit gösterimi !!!!!!!!!!!!!!!!!

kareler = [x**2 for x in range(1,11)]
print(f"sayılar: {kareler}")


import random

sayi = random.randint(1,6)
print(sayi)

#shuffle(LİST) => verilen listenin öğelerinin sırasının yerini değiştirir

isimler = ["Ahmet", "Ayşe", "Mehmet", "Elif", "Can"]
print("karıştırılmadan önce: ", isimler)

random.shuffle(isimler)
print("karıştırıldıktan sonra isimler: ", isimler)

"""
"""

isimler = ["ali", "ece", "merve", "semih", "arda", "kaan", "bora"]
numaralar = [131, 423, 231, 463, 523, 564, 745]

yeni_dizi = []

for isim, numara in zip(isimler, numaralar):
    yeni_dizi.append(isim + " " + str(numara))

print(yeni_dizi)
          
enb = enk = numaralar[0]
enb_index = enb_index = 0

for num in range(len(numaralar)):
    if (num < enk):
        enk = num
        enk_index = num
    
    if (num > enb):
        enb = num
        enb_index = num
    

print(f"numarası en büyük olan öğrenci: {yeni_dizi[enb_index]}")
print(f"numarası en küçük olan öğrenci: {yeni_dizi[enk_index]}")




while True:
    print("lütfen bir islem seciniz: ")
    print("1 - toplama")
    print("2 - çıkarma")
    print("3 - çarpma")
    print("4 - bölme")
    print("0 - çıkış")
    
    secim = int(input("bir işlem seçiniz:"))
    
    if secim == 0:
        print("hosca kalın")
        break
    
    a = float(input("1. sayıyı giriniz: "))
    b = float(input("1. sayıyı giriniz: "))

    
    if secim == 1:
        print(" işleminizin sonucu: ", a + b)
        
    if secim == 2:
        print(" işleminizin sonucu: ", a - b)
        
    if secim == 3:
        print(" işleminizin sonucu: ", a * b)
        
    if secim == 4:
        if b == 0:
            print("bir sayı sıfıra bölünemez")
        else:
            print(" işleminizin sonucu: ", a / b)

"""
"""    
import random

gunler = []
x = 0
toplam = 0

while x < 7:
    sicaklik = random.randint(1, 37)
    gunler.append(sicaklik)
    toplam += gunler[x]
    print(f"{x+1}. gün hava sıcaklığı {gunler[x]}'dir")
    x +=1

ortalama = toplam / len(gunler)
print(f"ortlama sıcaklık ise {ortalama} idir")
"""
"""
#tuple (demet) veri yapısı

#Listeler => Mutable(değiştirilebilir) ve order(sıarlı) idir
derslerLİst = ["fizik", "ingilizce", "matematik"]
derslerLİst[0] = "ingilizce"
print(derslerLİst)

#Tuple'ler,stringler => immutable(sonradan değiştirilemez) ve order idir
# mystring = "hello"
# mystring[0] = "z" (derlendiğinde TypeError verir)
derslerTuble = ("fizik", "ingilizce", "mstematik")

derslerTuble[0] = "ingilizce" 
# table ler sonradan değiştirilemezler bu yüzden saved edip çalıştırdığımızda 
# TypeError alırız

# eğer yaptığın yazılımda elemanların değiştirilmesini istemiyorsan immutable
# değiştirilebilir yapmak istiyorsan mutable tipleri kuplanmalısın

# bu durum sadece dizinin içindeki bir elemanın bir karakterei için geçerli değildir
# ayrıca list fonksiyonları append gibi fonksiyonlarda kullanılamaz
# sonuçta bir yılın mevsimleri bellidir x diye yeni bir mevsim olmaz 
# fakat index,len gibi ortak fonksiyonlara sahiptirler

"""
# [] => list, () => Truple, {} => SET {:} => Dictionary

"""
#SET (KÜME) VERİ YAPISI

derslerSet = {"Tarih", "Matematik", "Fizik"} #unorder(sırasızdır)
print(derslerSet) #çıktı sırası list ve traple gibi düzenli değil rast gele verilir
# ayrıca eleman sonradan eklenip çıkarışabilir fakat bir dizinin
# 2. elemaını nı ekle sil gibi değil
derslerSet.add("kimya")
derslerSet.add("ingilizce")
print(derslerSet)
print("fizik" in derslerSet) #true/false döndürür

sanatDersleriSet = {"Tarih", "piyano","futbol"}

#kesişim(intersection)
ortakDersler = derslerSet.intersection(sanatDersleriSet)
print(ortakDersler)

# Fark(difference)
dersFark = derslerSet.difference(sanatDersleriSet)
print(dersFark)

# BİRLEŞİM(union)
birlesim = derslerSet.union(sanatDersleriSet)
print(birlesim)
"""
""" 
import random
#Python Dictionary (SÖZLÜK) veri yapısı
# amacı anahtar ve değer lerin eşsiz eşlenmesini sağlamaktır
# örneğin tc ile vatandaş gibi herkesin kendine özel bir tc si vardır

ogrencilerDict = {100:"Ali kaya", 102:"Ali korkmaz", 103:"mehmet kaya"}
print(ogrencilerDict)

print(ogrencilerDict[100])

deger = ogrencilerDict.get(101) #get fonksiyonu eğer aranan eleman yoksa none değeri döndürür

if deger is None:
    print("aranılan öğrenci listede yok")
else:
    print("aranılan öğrenci mevcut")


for a in range(len(ogrencilerDict)):
    print(a)
    rastgele = random.randint(99, 104)
    deger = ogrencilerDict.get(rastgele)
    if deger is None:
        print(rastgele, deger)
        print("aranılan öğrenci listede yok")
    else:
        print(rastgele, deger)
        print("aranılan öğrenci mevcut")        
"""

# [] => list, () => Truple, {} => SET {:} => Dictionary


"""
def fonksiyonAdı():
    #işlem bloğu

"""

#SCOPE(KAPSAM)
#Bir fonksiyon içinde tanımlanan değişkenler yerel (lcoal) değişkenlerdir
#fonksiyonun dışında tanımlanan değşkenler ise global değişkenlerdir

"""
def ornek():
    x = 5 # yerel(local) değişken
    print("yerel x:", x) 

def ornek2():
    global x
    x*=2
    print("global x:", x)

x = 10
print("global x:", x)
ornek()
ornek2()
print("global x:", x)

"""

"""
def bol(x,y):
    a = x/y
    print(f"{x}/{y} = {a}")

def cıkar(x,y):
    a = x-y
    return a

    
bol(12,3)
print(cıkar(12,4))
"""

# Varsayılan parametre değerler (DEFAULT)
# parametre verilmezse varsayılan değer kullanılır
"""
def selamla(isim = "misafir"):
    print("merhaba", isim)
    
selamla ("ahmet")
selamla()
"""
#belirsiz sayıda parametre *args
"""
def toplam(*args):
 return sum(args)

def cikarma(*sayilar):
    sonuc = sayilar[0]   
    for sayi in sayilar[1:]:
        sonuc -= sayi
    return sonuc

print(cikarma(20, 5, 3))

print(toplam(1,2,3))
"""

# **kwargs, isimlşi bir sözlük (dict) olarak alır
# Bu sayede dinamik ve esnek fonskiyonlar yazabiliriz
# İçindeki anahtar (key) ve değer (value) çiftlerini kullanabliriz

"""
def kisiBilgileri(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    
kisiBilgileri(ad="semih", yas=25, sehir = "Malatya")
    
"""
"""
import random

def sayi_tahmin_oyunu():

    while True:

        # hak alma ve doğrulama
        while True:
            hak = input("Kaç tahmin hakkınız olsun? ")
            if hak.isdigit() and int(hak) > 0:
                hak = int(hak)
                break
            else:
                print("Lütfen pozitif bir sayı girin.")

        sayi = random.randint(0, 100)

        # oyun döngüsü
        while hak > 0:
            print(f"Kalan hak: {hak}")

            tahmin = input("Tahmininiz: ")

            if not tahmin.isdigit():
                print("Lütfen geçerli bir sayı girin.")
                continue

            tahmin = int(tahmin)

            if tahmin < 0 or tahmin > 100:
                print("0 ile 100 arasında bir sayı girin.")
                continue

            if tahmin < sayi:
                print("Tahmininiz küçük.")
            elif tahmin > sayi:
                print("Tahmininiz büyük.")
            else:
                print("Tebrikler! Bildiniz!")
                break

            hak -= 1

        if hak == 0:
            print(f"Hakkınız bitti. Doğru sayı: {sayi}")

        # tekrar kontrolü
        tekrar = input("Tekrar oynamak ister misiniz? (e/h): ").strip().lower()

        if tekrar != "e":
            print("Oyun bitti.")
            break


sayi_tahmin_oyunu()
"""
"""
class tesla:
    
    teslaSayısı = 0
    sisFari = 2 #sınıf değişkeni
    
    #renk = "beyaz"
    #batarya = "uzun yol"
    #jant = 20
    #otopilot = False
    def __init__(self, renk="beyaz", batarya = "uzun yol", jant = 20, otopilot = False):
        self.renk = renk #nesne değişkeni
        self.batarya = batarya #nesne değişkeni
        self.jant = jant #nesne değişkeni
        self.otopilot = otopilot #nesne değişkeni
        tesla.teslaSayısı += 1
    def bilgiGoster(self):
        print(f"Renk: {self.renk}, Batarya: {self.batarya}, Jant:{self.jant}")
    
    
benimTesla = tesla()
benimTesla.bilgiGoster()

benimTesla.jant = 21
print(benimTesla.renk, benimTesla.batarya, benimTesla.jant)

ayseninTesla = tesla(otopilot=True)
ayseninTesla.bilgiGoster()
print(ayseninTesla.otopilot)


#PascalCasea => TeslaOtomobil
    ayseninTesla.sisFari = 3 #3
    ayseninTesla.sunroof = True
    print(ayseninTesla.sun) 
    print("Tesla sis farlari: ", Tesla.sisFari) #2
    print("beim tesla: " benimTesla.sisFari) #2

"""    
""" 
class Tesla:   
    tesla_count = 0  # sınıf değişkeni
    sis_fari = 2     # sınıf değişkeni   
    gecerli_renkler = ["Beyaz", "Siyah", "Kırmızı"]    # sınıf değişkeni  
    gecerli_bataryalar = ["Uzun Menzil", "Kısa Menzil"]

    # initializer method
    def __init__(self, renk="Beyaz", batarya="Uzun Menzil", jant=20, otopilot=False):
        # Eğer verilen renk geçerli değilse varsayılan olarak "Beyaz" ayarlanır
        if renk in Tesla.gecerli_renkler:
            self.__renk = renk     # nesne değişkeni    
        else:
            self.__renk = "Beyaz"
        
        if batarya in Tesla.gecerli_bataryalar:
            self.__batarya = batarya    # nesne değişkeni        
        else:
            self.__batarya = "Uzun Menzil"
       
        if 19 <= jant <= 22:
            self.__jant = jant    # nesne değişkeni
        else:
            self.__jant = 20

        if isinstance(otopilot, bool):
            self.__otopilot = otopilot    # nesne değişkeni
        else: 
            self.__otopilot = False

        self.__hiz = 0         # nesne değişkeni
        Tesla.tesla_count += 1   # Tesla.tesla_count = Tesla.tesla_count + 1  
       
    def goster_bilgi(self):
        print(f"Renk: {self.__renk}, Batarya:{self.__batarya}, Jant:{self.__jant}," 
              f"Otopilot:{self.__otopilot}, Hız: {self.__hiz}")

    def hizlan(self, miktar):
        self.__hiz += miktar
    
    def yavasla(self, miktar):
        self.__hiz -= miktar
        if self.__hiz < 0:
            self.__hiz = 0

    # hiz getter
    def get_hiz(self):
        return self.__hiz

    # otopilot getter
    def get_otopilot(self):
        return self.__otopilot
    
    # otopilot setter
    def set_otopilot(self, yeni_otopilot):
        if isinstance(yeni_otopilot, bool):
            self.__otopilot = yeni_otopilot
        else:
            print("Dikkat! Otopilot değeir hatalı")

    # jant getter
    def get_jant(self):
        return self.__jant
    
    # jant setter
    def set_jant(self, yeni_jant):
        if 19 <= yeni_jant <= 22:
            self.__jant = yeni_jant
        else:
            print("Dikkat! yanlış jant değeri!")

    # batarya getter
    def get_batarya(self):
        return self.__batarya
    
    # batarya setter
    def set_batarya(self, yeni_batarya):
        if yeni_batarya in Tesla.gecerli_bataryalar:
            self.__batarya = yeni_batarya
        else:
            print("Dikkat! geçersiz batarya")


    # renk getter
    def get_renk(self):
        return self.__renk

    # renk setter
    def set_renk(self, yeni_renk):
        if yeni_renk in Tesla.gecerli_renkler:
            self.__renk = yeni_renk
        else:
            print("Dikkat! Geçersiz renk:", yeni_renk)


benim_teslam = Tesla(jant=21, renk="Siyah", batarya="Kısa Menzil")
benim_teslam.set_batarya("Uzun Menzil")
benim_teslam.set_otopilot(True)
benim_teslam.hizlan(70)
print("benim teslam:")
benim_teslam.goster_bilgi()
print("benim tesla otopilot:", benim_teslam.get_otopilot())


velinin_teslasi = Tesla(renk="Siyah", otopilot=True)
print("\nvelinin tesla:")
velinin_teslasi.goster_bilgi()

aysenin_teslasi = Tesla(otopilot=True)
print("\naysenin tesla:")
aysenin_teslasi.goster_bilgi()

"""
"""
class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        
    def ses_cikar(self):
        print("hayvan ses çıkarıyor")
        
    def kos(self):
        print(f"{self.isim} koşuyor..")
        
class kedi(Hayvan):
    def __init__(self, isim, yas,renk):
        super().__init__(isim, yas)
        self.renk = renk
    
    # Ata sınıfta tanımlanan bir şeyi alt sınıfta tekrar tanımlamaya 
    # Override  denir
    
    #Override
    def ses_cikar(self):
        print(f"{self.isim} miyavlıyor")
    
    def tırman(self):
        print(f"{self.isim} ağaca tırmanıyor")
        
class kopek(Hayvan):
    
    #Override
    def ses_cikar(self):
        super().ses_cikar()
        print(f"{self.isim} havlıyor")
        
    def koru(self):
        print(f"{self.isim} evi koruyor")
    
kedi1 = kedi("mercan", 13, "beyaz")

kopek1 = kopek("kömür", 15)

kedi1.tırman()
kopek1.ses_cikar()
kedi1.ses_cikar()
kedi1.kos()

print("kedinin rengi: ", kedi1.renk)
"""
"""
class Hayvan:
    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        
    def ses_cikar(self):
        print("hayvan ses çıkarıyor")
        
    def kos(self):
        print(f"{self.isim} koşuyor..")
        
class kedi(Hayvan):
    def __init__(self, isim, yas,renk):
        super().__init__(isim, yas)
        self.renk = renk
    
    # Ata sınıfta tanımlanan bir şeyi alt sınıfta tekrar tanımlamaya 
    # Override  denir
    
    #Override
    def ses_cikar(self):
        print(f"{self.isim} miyavlıyor")
    
    def tırman(self):
        print(f"{self.isim} ağaca tırmanıyor")
        
class kopek(Hayvan):
    
    #Override
    def ses_cikar(self):
        super().ses_cikar()
        print(f"{self.isim} havlıyor")
        
    def koru(self):
        print(f"{self.isim} evi koruyor")
#poliforfizm kullanmak için soyutlama-kapsulleme zorunlu değil
class Kus():
    def ses_cikar(self):
        print("cik cik cik")        

#poliforfizm
def hayvanKonustur(Hayvan):
    Hayvan.ses_cikar()
    
hayvan = Hayvan("genel",0)
kedi1 = kedi("pamuk", 3, "siyah")
kopek1 = kopek("karabaş", 5)
kedi2 = kedi("alev", 31, "albino")
kus1 = Kus()

hayvanKonustur(hayvan)
hayvanKonustur(kedi1)
hayvanKonustur(kopek1)
hayvanKonustur(kus1)
"""

"""
from abc import ABC, abstractmethod

#SOYUT sınıf tanımı
class Sekil(ABC):
    @abstractmethod
    def alanHesaplama(self):
        pass #alt sınıflar mutlaka bu methodu gerçekleştirmeli
        
#ALT sınıf tanımı
class kare(Sekil):
    def __init__(self,kenar):
        self.kenar = kenar
        
    def alanHesaplama(self):
        return self.kenar ** 2
    
class daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
        
    def alanHesaplama(self):
        return 3.14*(self.yaricap ** 2)

#Bu fonksiyon, Şekil arayüzüne (alanHesapla methoduna) güvenerek çalışır

def sekilAlanıYazdir(sekil):
    print(f"şeklin alanı {sekil.alanHesaplama()}")


kare1 = kare(4)
daire1 = daire(5)

sekilAlanıYazdir(daire1)
sekilAlanıYazdir(kare1)
"""

"""

import json

json_string = '{"ad": "Ahmet", "yas": 30, "sehir": ["İstanbul", "Ankara"]}'

# JSON stringini Python sözlüğüne (dict) dönüştürme
data = json.loads(json_string)

print(data)
print(data["ad"])
print(data["yas"])
print(data["sehir"])
print("Ahmetin gittiği şehir sayısı: ", len(data["sehir"]))
print(data["sehir"][0])

# Python sözlüğünü (dict) JSON stringine dönüştürme
data_dict = {
    "kişiler": [
        {"ad": "Ahmet", "yas": 30, "sehir": ["İstanbul", "Ankara"]},
        {"ad": "Ayşe", "yas": 25, "sehir": ["İzmir", "Bursa"]},
        {"ad": "Mehmet", "yas": 35, "sehir": ["Adana", "Gaziantep"]}
    ]
}

json_string = json.dumps(data_dict, ensure_ascii=False, indent=4) # ensure_ascii=False Türkçe karakterlerin düzgün görünmesini sağlar, indent=4 ise okunabilirliği artırır


print(json_string)

"""

"""

data_dict = {
    "kişiler": [
        {"ad": "Ahmet", "yas": 30, "sehir": ["İstanbul", "Ankara"]}
        {"ad": "Ayşe", "yas": 25, "sehir": ["İzmir", "Bursa"]},
        {"ad": "Mehmet", "yas": 35, "sehir": ["Adana", "Gaziantep"]}
    ]
}

# JSON verisini "data.json" dosyasına yazma

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data_dict, file, ensure_ascii=False, indent=4)

print(f"{len(data_dict['kişiler'])} kişi bilgisi data.json dosyasına kaydedildi.")

# "data.json" dosyasından JSON verisini okuma
with open("data.json", "r", encoding="utf-8") as file:
    data_from_file = json.load(file)

print("Dosyadan okunan veriler:")
for kisi in data_from_file["kişiler"]:
    print(f"Ad: {kisi['ad']}, Yaş: {kisi['yas']}, Şehirler: {', '.join(kisi['sehir'])}")

"""