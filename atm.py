def atm():
    kullaniciAdi = "Mervan"
    sifre = "1234"
    hak = 3
    while True:
        hak -= 1
        giris = input("Kullanıcı adını giriniz = ")
        girisSifre = input("Şifre giriniz = ")
        
        if kullaniciAdi == giris and sifre == girisSifre:
            bakiye = 5000
            while True:
                print("""İşlemler:
1 - Para çekme
2 - Para yatırma
3 - Şifre değiştirme
4 - Çıkış""")
                islem = int(input("Yapmak istediğiniz işlemi yazınız = "))
                if islem == 1:
                    while True:
                        cek = int(input("Çekmek istediğiniz miktarı yazınız = "))
                        if cek > bakiye:
                            print("Yetersiz bakiye..")
                        else:
                            bakiye -= cek
                            print("Güncel Bakiyeniz =", bakiye)
                            break
                elif islem == 2:
                    yatir = int(input("Yatırmak istediğiniz miktarı yazınız = "))                    
                    bakiye += yatir
                    print("Güncel bakiyeniz =", bakiye)
                elif islem == 3:
                    while True:
                        yeniSifre = input("Şifrenizi giriniz = ")
                        if yeniSifre == sifre:
                            yeniSifre = input("Yeni şifrenizi giriniz = ")
                            sifre = yeniSifre
                            print("Şifreniz güncellendi...")
                            break
                        else:
                            print("Yanlış girdiniz. Tekrar deneyiniz...")
                elif islem == 4:
                    print("Çıkış yapılıyor...")
                    print("Menüden çıkış yapmak için enter'a basınız")
                    break

        elif giris == "" and girisSifre == "":
            print("Çıkış yapılıyor..")           
            break

        elif hak == 0:
            print("Hakkınız bitti.")
            break
        else:
            print("Kullanıcı adı veya şifre hatalı..", hak)