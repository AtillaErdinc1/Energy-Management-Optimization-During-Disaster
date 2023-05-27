import matplotlib.pyplot as plt
import numpy as np
import random

avg_point = 0
avg_point_control = 1
print_control = 1

class Dugum:
    def __init__(self, ID, puan, enerji, jenerator):
        self.ID = ID
        self.puan = puan
        self.enerji = enerji
        self.jenerator = jenerator
        self.yukari = None
        self.asagi = None
        self.ileri = None
        self.geri = None


class CiftYonluBagliListe:
    def __init__(self):
        self.bas = None

    def dugum_ekle(self):
        yeni_dugum = Dugum(0, 0, 1, 1)

        yeni_dugum.ileri = Dugum(1, 0, 0, 0)
        yeni_dugum.ileri.ileri = Dugum(2, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri = Dugum(3, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.yukari = Dugum(19, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.yukari.ileri = Dugum(20, 1, 0, 0)
        yeni_dugum.ileri.ileri.ileri.yukari.ileri.ileri = Dugum(21, 1, 0, 0)
        yeni_dugum.ileri.ileri.ileri.yukari.ileri.ileri.ileri = Dugum(22, 5, 0, 0)
        yeni_dugum.ileri.ileri.ileri.yukari.ileri.ileri.asagi = Dugum(23, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.yukari.ileri.ileri.asagi.ileri = Dugum(24, 1, 0, 0)
        yeni_dugum.ileri.ileri.ileri.yukari.ileri.ileri.asagi.ileri.ileri = Dugum(25, 1, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri = Dugum(4, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri = Dugum(5, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(6, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari = Dugum(26, 5, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari.ileri = Dugum(27, 5, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari.ileri.ileri = Dugum(28, 5, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari.ileri.ileri.ileri = Dugum(29, 5, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari.ileri.ileri.ileri.ileri = Dugum(30, 8, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari.ileri.ileri.ileri.ileri.ileri = Dugum(31, 7, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(32, 5, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.yukari.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(33, 1, 0, 0)        
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(7, 1, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(8, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(9, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(10, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(11, 6, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(12, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(13, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(14, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(15, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(16, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(17, 0, 0, 0)
        yeni_dugum.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri.ileri = Dugum(18, 0, 0, 0)

                
        

        if self.bas is None:
            self.bas = yeni_dugum
        else:
            suan = self.bas
            while suan.ileri:
                suan = suan.ileri
            suan.ileri = yeni_dugum
            yeni_dugum.geri = suan

    def listele(self, dugum):
        if dugum is None:
            return []

        sonuc = [(dugum.ID, dugum.puan, dugum.enerji)]
        sonuc += self.listele(dugum.asagi)
        sonuc += self.listele(dugum.ileri)
        sonuc += self.listele(dugum.yukari)
        
        return sonuc

    def baslangic_listele(self):
        self.toplam = 0
        sonuc = self.listele(self.bas)
            #print(dugum[0], dugum[1], dugum[2])
        return sonuc  # Değerleri return ile geri döndür

 
    def enerji_degistir(self, dugum, enerji):
        if dugum is None:
            return

        if dugum.ID in self.secilen_dugumler:
            dugum.enerji = enerji
        
        self.enerji_degistir(dugum.asagi, enerji)
        self.enerji_degistir(dugum.ileri, enerji)
        self.enerji_degistir(dugum.yukari, enerji)
        
    def revize_et(self, adet=5):
        dugum_sayisi = 34
        self.secilen_dugumler = random.sample(range(1, dugum_sayisi+1), adet)
        enerji = 1
        for secilen_dugum in self.secilen_dugumler:
            self.enerji_degistir(self.bas, enerji)
            #print("Düğüm {} enerji değeri: {}".format(secilen_dugum, enerji))
        #self.baslangic_listele()
        
    def baglanti_kopar(self, adet=5):
        dugum_sayisi = 34
        self.secilen_dugumler = random.sample(range(1, dugum_sayisi+1), adet)
        enerji = 2  # Değiştirilen enerji değeri
        for secilen_dugum in self.secilen_dugumler:
            self.enerji_degistir(self.bas, enerji)
            #print("Düğüm {} enerji değeri: {}".format(secilen_dugum, enerji))
        #self.baslangic_listele()

plt.ion()

plt.xlabel('Eleman')
plt.ylabel('Sayı')
plt.title('Liste Elemanlarının Toplam Frekansı')
plt.grid(True)

unique_elements = np.arange(0, 34)
total_counts = np.zeros_like(unique_elements)

plt.plot(unique_elements, total_counts, 'b-')

plt.show()  # Grafik pencerisini gösterme
 
# Örnek kullanım
while True:
    toplam_puan = 0
    
    liste = CiftYonluBagliListe()
    liste.dugum_ekle()

    liste.revize_et(5)
    liste.baglanti_kopar(5)

    result = liste.baslangic_listele()
    
    sorted_tuple = sorted(result, key=lambda x: x[0])

    hat1 = sorted_tuple[0],sorted_tuple[1],sorted_tuple[2],sorted_tuple[3],sorted_tuple[23],sorted_tuple[24],sorted_tuple[25]
    hat2 = sorted_tuple[0],sorted_tuple[1],sorted_tuple[2],sorted_tuple[19],sorted_tuple[20],sorted_tuple[21],sorted_tuple[22]
    hat3 = sorted_tuple[0],sorted_tuple[1],sorted_tuple[2],sorted_tuple[3],sorted_tuple[4],sorted_tuple[5],sorted_tuple[6],sorted_tuple[26],sorted_tuple[27],sorted_tuple[28],sorted_tuple[29],sorted_tuple[30],sorted_tuple[31],sorted_tuple[32],sorted_tuple[33],
    hat4 = sorted_tuple[0],sorted_tuple[1],sorted_tuple[2],sorted_tuple[3],sorted_tuple[4],sorted_tuple[5],sorted_tuple[6],sorted_tuple[7],sorted_tuple[8],sorted_tuple[9],sorted_tuple[10],sorted_tuple[11],sorted_tuple[12],sorted_tuple[13],sorted_tuple[14],sorted_tuple[15],sorted_tuple[16],sorted_tuple[17],sorted_tuple[18]
    
    reverse_sorted_hat_1 = sorted(hat1, key=lambda x: x[0], reverse=True)
    reverse_sorted_hat_2 = sorted(hat2, key=lambda x: x[0], reverse=True)
    reverse_sorted_hat_3 = sorted(hat3, key=lambda x: x[0], reverse=True)
    reverse_sorted_hat_4 = sorted(hat4, key=lambda x: x[0], reverse=True)
 
    cells = []
    brakes = []
 
    total_point = 0
    energy_control = 0
    point_control = 0
    
    for i in reverse_sorted_hat_1:
        
        if(i[2]==1):
            cells.append(i[0])
        
        if(i[2]!=2):
            if(i[2]==1):
                energy_control = 1
            point_control = point_control + i[1]
        else:
            if i[0] not in brakes:
                brakes.append(i[0])
            break

    if(energy_control == 1):
        total_point = total_point + point_control
    energy_control = 0    
    point_control = 0
    
    for i in reverse_sorted_hat_2:
        
        if(i[2]==1):
            cells.append(i[0])
        if(i[2]!=2):
            if(i[2]==1):
                energy_control = 1
            point_control = point_control + i[1]
        else:
            if i[0] not in brakes:                
                brakes.append(i[0])
            break
        
    if(energy_control == 1):
        total_point = total_point + point_control
    energy_control = 0    
    point_control = 0
    
    for i in reverse_sorted_hat_3:
        if(i[2]==1):
            cells.append(i[0])
        if(i[2]!=2):
            if(i[2]==1):
                energy_control = 1
            point_control = point_control + i[1]
        else:
            if i[0] not in brakes:
                brakes.append(i[0])
            break
    
    if(energy_control == 1):
        total_point = total_point + point_control
    energy_control = 0    
    point_control = 0
    
    for i in reverse_sorted_hat_4:
        if(i[2]==1):
            cells.append(i[0])
        if(i[2]!=2):
            if(i[2]==1):
                energy_control = 1
            point_control = point_control + i[1]
        else:
            if i[0] not in brakes:
                brakes.append(i[0])
            break
    
    if(energy_control == 1):
        total_point = total_point + point_control
    energy_control = 0    
    point_control = 0
        
    if(total_point>57):
        print("HATA")
        
    min_brake_control = 33
    max_brake_control = 0
    

    

        
    for i in range(0,len(brakes),1):
        if(brakes[i]<min_brake_control):
            min_brake_control = brakes[i]
        if(brakes[i]>max_brake_control):
            max_brake_control = brakes[i]
    
    if(len(cells)==5 and len(brakes)>=4 and total_point>30 and total_point<45 and min_brake_control>=5 and max_brake_control<33):
        avg_point = avg_point + total_point
        print(str(print_control)+".tur"+" Tur puanı : "+str(total_point)+" Ortalama puan : "+str((avg_point/avg_point_control)))
        print_control = print_control + 1
        avg_point_control = avg_point_control +1
    
        new_counts = np.bincount(cells, minlength=len(unique_elements))
    
        total_counts += new_counts  # Toplam frekansları güncelle
    
        plt.clf()  # Önceki çizimi temizle
    
        plt.plot(unique_elements, total_counts, 'b-')
        plt.ylim(0, max(total_counts) + 1)  # Y ekseni sınırlarının güncellenmesi
        
        plt.draw()
        plt.pause(0.1)
    
    
    