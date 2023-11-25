from time import sleep

class Computer():

    def __init__(self,GPU = "Yok",motherboard = "Yok",CPU = "Yok",ram = 0,SSD = 0,işletim_sistemi = "Yok"):
        self.GPU = GPU
        self.motherboard = motherboard
        self.CPU = CPU
        self.ram = ram
        self.SSD = SSD
        self.işletim_sistemi = işletim_sistemi

    def format_at(self,cevap):
        if cevap == "Evet":
            print("Bilgisayar Formatlanıyor...")
            sleep(3)
            print("Bilgisayar Formatlandı.")
            self.işletim_sistemi = "Yok"
            a = input("İşletim Sistemi Kurmak İster misiniz?[Evet/Hayır]")
            if a == "Evet":
                b = input("Kurmak istediğiniz işletim sistemini girin:")
                self.işletim_sistemi = b
                sleep(1)
                print("Bilgisayarınızın Yeni İşletim sistemi:",b)
            elif a == "Hayır":
                print("İşletim sistemi kurulamadı.Lütfen daha Sonra Kurunuz.")
            else:
                print("geçersiz İşlem")
        elif cevap == "Hayır":
            print("Format Atılamadı.")
        else:
            print("geçersiz İşlem")

    def işletim_sistemi_kur(self,kurulacak_işletim_sistemi):
        if self.işletim_sistemi == "Yok":
            self.işletim_sistemi = kurulacak_işletim_sistemi
            print("İşletim sistemi başarıyla kuruldu.\nYeni işletim sisteminiz:",kurulacak_işletim_sistemi)
        elif len(self.işletim_sistemi) == 1:
            print("halihazırda bir işletim sistemi kurulu.\nLütfen ilk önce format atınız...")

    def GPU_değiştir(self,yeni_gpu):
        print("Ekran Kartı Değiştirildi.\nYeni Ekran Kartı:",yeni_gpu)
        self.GPU = yeni_gpu

    def anakart_değiştir(self,yeni_anakart):
        print("Anakart Değiştirildi.\nYeni Anakart:",yeni_anakart)
        self.motherboard = yeni_anakart

    def CPU_değiştir(self,yeni_cpu):
        print("İşlemci Değiştirildi.\nYeni İşlemci:",yeni_cpu)
        self.CPU = yeni_cpu

    def ram_ekle(self,yeni_ram):
        print("Ram Eklendi.\nYeni ram:",yeni_ram)
        self.ram += yeni_ram

    def ram_çıkar(self,çıkarılacak_ram):
        print("Ram Çıkartıldı.\nYeni ram:",çıkarılacak_ram)
        self.ram -= çıkarılacak_ram

    def SSD_ekle(self,yeni_ssd):
        print("SSD Eklendi.\nYeni SSD:",yeni_ssd)
        self.SSD += yeni_ssd

    def SSD_çıkar(self,çıkarılacak_ssd):
        print("SSD çıkartıldı.\nYeni SSD:",çıkarılacak_ssd)
        int(self.SSD)
        int(çıkarılacak_ssd)
        self.SSD -= çıkarılacak_ssd

    def bellek_temizle(self):
        print("Bellek Temizleniyor..")
        sleep(2)
        print("Bellek Temizlendi.")

    def __str__(self):
        sleep(1)
        return """************************
GPU: {}\nMotherboard: {}\nCPU: {}\nRam: {}\nSSD: {}\nİşletim Sistemi: {}
************************
""".format(self.GPU,self.motherboard,self.CPU,self.ram,self.SSD,self.işletim_sistemi)

print("""*************************************

Bilgisayar Uygulaması

işlemler;

1.Format Atma

2.İşletim Sistemi Kurma

3.Ekran Kartı Değiştirme/Takma

4.Anakart Değiştirme/Takma

5.İşlemci Değiştirme/Takma

6.Ram Ekleme

7.Ram Çıkartma

8.SSD Genişletme

9.SSD Çıkartma

10.Bellek Temizle

11.Bilgisayar Bilgileri

Çıkış için 'q'yu tuşlayın.

*************************************
""")

bilgisayar = Computer()

while True:
    işlem = input("İşlemi Girin:")
    if işlem == "q":
        break
    elif işlem == "1":
        cevap = input("Bilgisayarınızdaki Tüm Bilgiler Silinecektir.Emin misiniz?[Evet/Hayır]")
        bilgisayar.format_at(cevap)
    elif işlem == "2":
        kurulacak_işletim_sistemi = input("Kurulacak İşletim sisteminin Adını girin:")
        bilgisayar.işletim_sistemi_kur(kurulacak_işletim_sistemi)
    elif işlem == "3":
        yeni_kart = input("Yeni Ekran Kartının Modelini Girin:")
        bilgisayar.GPU_değiştir(yeni_kart)
    elif işlem == "4":
        yeni_anakart = input("Yeni Anakartın Modelini Girin:")
        bilgisayar.anakart_değiştir(yeni_anakart)
    elif işlem == "5":
        yeni_işlemci = input("Yeni İşlemcinin Modelini Girin:")
        bilgisayar.CPU_değiştir(yeni_işlemci)
    elif işlem == "6":
        ram_ekle = int(input("Eklemek İstediğiniz Ram Kaç gb:"))
        bilgisayar.ram_ekle(ram_ekle)
    elif işlem == "7":
        ram_çıkart = int(input("Çıkartmak İstediğiniz Ram Kaç gb:"))
        bilgisayar.ram_çıkar(ram_çıkart)
    elif işlem == "8":
        ssd_ekle = int(input("Eklemek İstediğiniz SSD Kaç gb:"))
        bilgisayar.SSD_ekle(ssd_ekle)
    elif işlem == "9":
        ssd_çıkart = int(input("Çıkartmak İstediğiniz SSD Kaç gb:"))
        bilgisayar.SSD_çıkar(ssd_çıkart)
    elif işlem == "10":
        bilgisayar.bellek_temizle()
    elif işlem == "11":
        print(bilgisayar)
    else:
        print("Geçersiz İşlem.")