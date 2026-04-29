class Ogrenci:

    def __init__(self, ad, soyad, numara, notlar=None):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
        self.notlar = notlar if notlar is not None else []

    def notGir(self, notu):
        if 0 <= notu <= 100:
            self.notlar.append(notu)
        else:
            print("Not 0-100 arasında olmalıdır.")


class Okul:

    def __init__(self):
        self.ogrenciler = {}
        self.dosyadanYukle()

    # DOSYADAN VERİ OKUMA
    def dosyadanYukle(self):

        try:
            with open("ogrenciler.txt", "r") as f:

                for satir in f:
                    parcalar = satir.strip().split(";")

                    if len(parcalar) != 4:
                        continue

                    ad, soyad, numara, notlar = parcalar

                    if notlar:
                        not_listesi = list(map(float, notlar.split(",")))
                    else:
                        not_listesi = []

                    ogrenci = Ogrenci(ad, soyad, numara, not_listesi)
                    self.ogrenciler[numara] = ogrenci

        except FileNotFoundError:
            print("Dosya bulunamadı.")

    # DOSYAYA KAYDETME
    def dosyayaKaydet(self):

        try:
            with open("ogrenciler.txt", "w") as f:

                for ogrenci in self.ogrenciler.values():

                    notlar = ",".join(map(str, ogrenci.notlar))

                    f.write(f"{ogrenci.ad};{ogrenci.soyad};{ogrenci.numara};{notlar}\n")

        except Exception as e:
            print("Dosyaya kaydetme hatası:", e)

    def ogrenciEkle(self, ad, soyad, numara):

        if numara in self.ogrenciler:
            print("Bu öğrenci numarası zaten mevcut.")
            return

        yeni_ogrenci = Ogrenci(ad, soyad, numara)

        self.ogrenciler[numara] = yeni_ogrenci

        self.dosyayaKaydet()

        print("Öğrenci başarıyla eklendi.")

    def ogrenciSil(self, numara):

        if numara in self.ogrenciler:

            del self.ogrenciler[numara]

            self.dosyayaKaydet()

            print("Öğrenci silindi.")

        else:
            print("Bu öğrenci bulunamadı.")

    def ogrenciBilgileriniGoruntule(self, numara):

        if numara in self.ogrenciler:

            ogrenci = self.ogrenciler[numara]

            print("\nÖğrenci Bilgileri")
            print("Ad:", ogrenci.ad)
            print("Soyad:", ogrenci.soyad)
            print("Numara:", ogrenci.numara)
            print("Notlar:", ogrenci.notlar)
            print("-------------------")

        else:
            print("Bu öğrenci bulunamadı.")

    def ogrencileriListele(self):

        if not self.ogrenciler:
            print("Hiç öğrenci yok.")
            return

        print("\nTüm Öğrenciler\n")

        for ogrenci in self.ogrenciler.values():

            print(
                ogrenci.ad,
                ogrenci.soyad,
                ogrenci.numara,
                ogrenci.notlar
            )

    def notGir(self, numara, notu):

        if numara in self.ogrenciler:

            self.ogrenciler[numara].notGir(notu)

            self.dosyayaKaydet()

            print("Not eklendi.")

        else:
            print("Öğrenci bulunamadı.")

    def okulOrtalamasi(self):

        toplam = 0
        sayi = 0

        for ogrenci in self.ogrenciler.values():

            for notu in ogrenci.notlar:
                toplam += notu
                sayi += 1

        if sayi == 0:
            print("Henüz not girilmemiş.")
        else:
            ortalama = toplam / sayi
            print("Okul ortalaması:", round(ortalama, 2))


okul = Okul()


while True:

    print("\nÖĞRENCİ BİLGİ SİSTEMİ")
    print("1 - Öğrenci Ekle")
    print("2 - Öğrenci Sil")
    print("3 - Öğrencileri Listele")
    print("4 - Öğrenci Bilgisi Görüntüle")
    print("5 - Not Gir")
    print("6 - Okul Ortalaması")
    print("7 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":

        ad = input("Ad: ")
        soyad = input("Soyad: ")
        numara = input("Numara: ")

        okul.ogrenciEkle(ad, soyad, numara)

    elif secim == "2":

        numara = input("Silinecek öğrenci numarası: ")
        okul.ogrenciSil(numara)

    elif secim == "3":

        okul.ogrencileriListele()

    elif secim == "4":

        numara = input("Öğrenci numarası: ")
        okul.ogrenciBilgileriniGoruntule(numara)

    elif secim == "5":

        numara = input("Öğrenci numarası: ")

        try:
            notu = float(input("Not (0-100): "))
            okul.notGir(numara, notu)
        except ValueError:
            print("Geçerli bir sayı giriniz.")

    elif secim == "6":

        okul.okulOrtalamasi()

    elif secim == "7":

        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz seçim.")