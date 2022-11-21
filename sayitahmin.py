import random
def sayiTahmin():
    sayi = random.randint(1,100)
    hak = 7
    """sayi = [i for i in range(100)]
    tutulanSayi = random.choice(saysi) """
    while True:
        hak -=1
        tahmin = int(input("Bir sayı giriniz = "))
        if tahmin == sayi:
            print("Tebrikler bildiniz... Kalan Haklarınız =", hak)
            print("Sayı = ", sayi)
            break
        elif tahmin != sayi:
            if tahmin > sayi:
                print("Tuttuğunuz sayı yüksek. Azaltın")
            elif tahmin < sayi:
                print("Tuttuğunuz sayı düşük. Yükseltin")
        elif hak == 0:
            print("Haklarınız bitti")
            print("Tutulan sayı =", sayi)
            break
            
sayiTahmin()