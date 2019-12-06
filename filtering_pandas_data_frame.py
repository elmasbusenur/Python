# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:16:39 2019

@author: PC
"""


import pandas as pd
dictionary={"Name":["Ali","Buse","Selma","Hakan","Bülent","Yağmur","Ahmet"],
            "Age":[18,45,12,36,40,18,63],
            "Maas":[100,200,400,500,740,963,123]}

dataFrame1=pd.DataFrame(dictionary)
dataFrame1["Şehir"]=["İstanbul","Bursa","Eskişehir","Konya","Siirt","Ankara","Kayseri"]

filtre1=dataFrame1.Maas>200
filtre2=dataFrame1.Age<20

filtrelenmemiş_data=dataFrame1[filtre1]


filtrelenmemiş_data=dataFrame1[filtre2]

dataFrame1[filtre1 & filtre2]
print(dataFrame1[filtre1 & filtre2])