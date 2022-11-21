class HavaYollari:
    def __init__(self, inis, kalkis, kapasite):
        self.inis = inis
        self.kalkis = kalkis
        self.kapasite = kapasite
        
    def bilgi(self):
        self.obje = self.inis, self.kalkis, self.kapasite
        for i in self.obje:
            print(i)

class TurkHavaYollari(HavaYollari):
    def __init__(self, inis, kalkis, kapasite, seferNo, ucret):
        super().__init__(inis, kalkis, kapasite)
        self.sefer = seferNo
        self.ucret = ucret
    
    def bilgi(self):
        self.obje = self.inis, self.kalkis, self.kapasite, self.sefer, self.ucret 
        for i in self.obje:
            print(i)
    def degis(self):
        while True:
            print("""İşlemler:
inis
kalkiş""")
            islem = input("değiştirmek istediğiniz parametreyi yazınız = ")
            if islem == "inis":
                rotar1 = input("Güncel bilgiyi giriniz = ")
                self.inis = rotar1
                print("Bilgiler güncellendi. Yeni iniş yeri =", self.inis)
            elif islem == "kalkiş":
                rotar2 = input("Güncel bilgiyi giriniz = ")
                self.kalkis = rotar2
                print("Bilgiler güncellendi. Yeni kalkış yeri =", self.kalkis)
            elif islem == "":
                print("Çıkış yapılıyor")
                break
            else:
                print("Geçersiz parametre")
        

ilkUcak = TurkHavaYollari("Ankara", "İstanbul", 500, 13456, 5000)
""" ilkUcak.bilgi()
ilkUcak.degis()
ilkUcak.bilgi() """
