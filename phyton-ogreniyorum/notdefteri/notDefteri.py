def notEkle():
    with open("notDefteri.txt", "a") as f:
        notlar = input("Notunuzu giriniz: ")
        f.write(notlar + "\n")


def notlariGoruntule():
    try:
        with open("notDefteri.txt", "r") as f:
            notlar = f.readlines()

            if notlar:
                print("Notlarınız:")

                for notu in notlar:
                    print(notu.strip())

            else:
                print("Henuz not girilmemis.")

    except FileNotFoundError:
        print("Henüz not girilmemiş.")


def notlariTemizle():
    with open("notDefteri.txt", "w"):
        pass

    print("Notlar temizlendi.")


def menu():

    while True:

        print("\nNot Defteri Uygulamasi")
        print("1. Not Ekle")
        print("2. Notlari Goruntule")
        print("3. Notlari Temizle")
        print("4. Cikis")

        secim = input("Seciminizi yapınız: ")

        if secim == "1":
            notEkle()

        elif secim == "2":
            notlariGoruntule()

        elif secim == "3":
            notlariTemizle()

        elif secim == "4":
            print("Cıkıs yapılıyor...")
            break

        else:
            print("Gecersiz secim")


menu()