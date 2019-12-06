# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 09:19:40 2019

@author: PC
"""
"""

liste=[7,2,6,9,-9]
mini=456545

for each in liste:
    if(each<mini):
        mini=each
    else:
        continue
print(mini)
"""
class Calisan:
    zam_oranı=1.8
    counter=0
    def __init__(self,isim,soyisim,maas): # constructor
        
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.email = isim+soyisim+"@asd.com"
        Calisan.counter=Calisan.counter+1
    
    def giveNameSurname(self):
        return self.isim +" " +self.soyisim
    
    def zam_yap(self):
        self.maas=self.maas+self.maas*self.zam_oranı
calisan1=Calisan("ali","ak",100)
print("ilk maas:",calisan1.maas)
calisan1.zam_yap()
print("yeni maas:",calisan1.maas)
calisan2=Calisan("ayse","yaz", 250)
print(calisan1.isim,calisan1.soyisim,calisan1.counter)
print(calisan2.isim,calisan2.soyisim,calisan2.counter)

calisan3=Calisan("fatma","kara", 8990)
print(calisan3.isim,calisan3.soyisim,calisan3.counter)


calisan4=Calisan("selma","dogan", 290)
print(calisan4.isim,calisan4.soyisim,calisan4.counter)

Calisan.counter

liste=[calisan1,calisan2,calisan3,calisan4]
maxi_maas=-1
index=-1
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas=each.maas
        index=each
print(maxi_maas)
print("en yüksek maas:",index.giveNameSurname())
#isci1 = Calisan("ali", "veli",100) 
#print(isci1.maas)
#print(isci1.giveNameSurname())
        