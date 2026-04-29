"""
Öğrenci Bilgi Sistemi
"""


class Ogrenci:
    def __init__(self, ad, soyad, numara, sinif, notlar=None):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.sinif = sinif
        self.notlar = notlar if notlar is not None else []

    def notGir(self, notu):
        if 0 <= notu <= 100:
            self.notlar.append(notu)
        else:
            print("Not 0-100 arasında olmalıdır.")

    def ogrenciBilgileriniGoruntule(self):
        print(f"Ad: {self.ad}")
        print(f"Soyad: {self.soyad}")
        print(f"Numara: {self.numara}")
        print(f"Sınıf: {self.sinif}")
        print(f"Notlar: {self.notlar}")
        print("------------------------")

    def ogrenciGuncelle(self, ad, soyad, sinif):
        if ad:
            self.ad = ad
        if soyad:
            self.soyad = soyad
        if sinif:
            self.sinif = sinif


ogrencilerDict = {}


def ogrenciEkle():
    ad = input("Ad: ")
    soyad = input("Soyad: ")
    numara = input("Öğrenci Numarası: ")
    sinif = input("Sınıf: ")

    if numara in ogrencilerDict:
        print("Bu öğrenci numarası zaten mevcut.")
        return

    ogrenci = Ogrenci(ad, soyad, numara, sinif)
    ogrencilerDict[numara] = ogrenci
    print("Öğrenci başarıyla eklendi.")


def ogrenciSil():
    numara = input("Silinecek öğrenci numarası: ")

    if numara in ogrencilerDict:
        del ogrencilerDict[numara]
        print("Öğrenci silindi.")
    else:
        print("Bu öğrenci bulunamadı.")


def ogrenciListele():
    if not ogrencilerDict:
        print("Hiç öğrenci yok.")
        return

    for ogrenci in ogrencilerDict.values():
        ogrenci.ogrenciBilgileriniGoruntule()


def notGir():
    numara = input("Not girilecek öğrenci numarası: ")

    if numara in ogrencilerDict:
        try:
            notu = float(input("Not (0-100): "))
            ogrencilerDict[numara].notGir(notu)
            print("Not eklendi.")
        except ValueError:
            print("Geçerli bir sayı giriniz.")

    else:
        print("Bu öğrenci bulunamadı.")


def ogrenciGuncelle():
    numara = input("Güncellenecek öğrenci numarası: ")

    if numara in ogrencilerDict:
        ad = input("Yeni ad (boş bırakılabilir): ")
        soyad = input("Yeni soyad (boş bırakılabilir): ")
        sinif = input("Yeni sınıf (boş bırakılabilir): ")

        ogrencilerDict[numara].ogrenciGuncelle(ad, soyad, sinif)
        print("Güncelleme yapıldı.")

    else:
        print("Bu öğrenci bulunamadı.")


def okulOrtalamasi():
    toplam = 0
    sayi = 0

    for ogrenci in ogrencilerDict.values():
        sayi += 1
        for notu in ogrenci.notlar:
            toplam += notu

    if sayi > 0:
        ortalama = toplam / sayi
        print(f"Okul ortalaması: {ortalama:.2f}")
    else:
        print("Henüz not girilmemiş.")


while True:

    print("\nÖĞRENCİ BİLGİ SİSTEMİ")
    print("1 - Öğrenci Ekle")
    print("2 - Öğrenci Sil")
    print("3 - Öğrenci Listele")
    print("4 - Öğrenci Güncelle")
    print("5 - Not Gir")
    print("6 - Öğrenci Bilgisi Görüntüle")
    print("7 - Okul Ortalaması")
    print("8 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenciEkle()

    elif secim == "2":
        ogrenciSil()

    elif secim == "3":
        ogrenciListele()

    elif secim == "4":
        ogrenciGuncelle()

    elif secim == "5":
        notGir()

    elif secim == "6":
        numara = input("Öğrenci numarası: ")

        if numara in ogrencilerDict:
            ogrencilerDict[numara].ogrenciBilgileriniGoruntule()
        else:
            print("Öğrenci bulunamadı.")

    elif secim == "7":
        okulOrtalamasi()

    elif secim == "8":
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")