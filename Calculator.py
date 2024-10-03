import math


class Hesapmakinesi:
    def __init__(self):
        self.hafiza = 0

    def toplama(self, sayi):
        self.hafiza += sayi
        return self.hafiza

    def cikarma(self, sayi):
        self.hafiza -= sayi
        return self.hafiza

    def carpma(self, sayi):
        self.hafiza *= sayi
        return self.hafiza

    def bolme(self, sayi):
        if sayi == 0:
            return "Sayı sıfıra bölünemez."
        self.hafiza /= sayi
        return self.hafiza

    def karekok_al(self):
        if self.hafiza < 0:
            return "Negatif sayının karekökü alınamaz."
        self.hafiza = math.sqrt(self.hafiza)
        return self.hafiza

    def yuzde(self, sayi):
        self.hafiza = self.hafiza * (sayi / 100)
        return self.hafiza

    def grand_total(self):
        return self.hafiza

    def reset(self):
        self.hafiza = 0


if __name__ == "__main__":
    hesapmakinesi = Hesapmakinesi()

    while True:
        print("\n1. Toplama\n2. Çıkarma\n3. Çarpma\n4. Bölme\n5. Karekök\n6. Yüzde\n7. Grand Total\n8. Hesap Makinesini Sıfırla\n9. Çıkış")
        try:
            secim = int(input("Lütfen bir işlem seçin: "))
        except ValueError:
            print("Yanlış bir işlem tuşladınız.")
            continue

        if secim == 9:
            print("Hesap Makinesinden Çıkış Yapıldı.")
            break

        if secim in [1, 2, 3, 4]:
            if hesapmakinesi.hafiza == 0:
                sayi1 = float(input("Birinci sayıyı girin :  "))
                hesapmakinesi.hafiza = sayi1
            else:
                sayi1 = hesapmakinesi.grand_total()

            sayi2 = float(input("İkinci sayıyı girin: "))
        elif secim == 5:
            sayi1 = hesapmakinesi.grand_total() if hesapmakinesi.hafiza != 0 else float(input("Karekök almak istediğiniz sayıyı girin: "))
            sayi2 = None
        elif secim == 6:
            sayi1 = hesapmakinesi.grand_total() if hesapmakinesi.hafiza != 0 else float(input("Yüzde almak istediğiniz sayıyı girin: "))
            sayi2 = float(input("Yüzde oranını girin: "))
        elif secim == 7:
            print("Grand Total:", hesapmakinesi.grand_total())
            continue
        elif secim == 8:
            hesapmakinesi.reset()
            print("Hesap makinesi sıfırlandı.")
            continue
        else:
            print("Geçersiz seçim.")
            continue

        try:
            if secim == 1:
                result = hesapmakinesi.toplama(sayi2)
            elif secim == 2:
                result = hesapmakinesi.cikarma(sayi2)
            elif secim == 3:
                result = hesapmakinesi.carpma(sayi2)
            elif secim == 4:
                result = hesapmakinesi.bolme(sayi2)
            elif secim == 5:
                result = hesapmakinesi.karekok_al()
            elif secim == 6:
                result = hesapmakinesi.yuzde(sayi2)

            print("Sonuç:", result)

        except ValueError:
            print("Geçersiz Giriş.")
        except ZeroDivisionError:
            print("Sıfıra Bölme Hatası.")
        except:
            print("Bir Hata Oluştu.")
