# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 11:14:27 2019

@author: PC
"""


import pandas as pd
dictionary={"Name":["Ali","Buse","Selma","Hakan","Bülent","Yağmur","Ahmet"],
            "Age":[18,45,12,36,40,18,63],
            "Maas":[100,200,400,500,740,963,123]}

dataFrame1=pd.DataFrame(dictionary)

print(dataFrame1["Name"])

print(dataFrame1["Age"])

dataFrame1["Şehir"]=["İstanbul","Bursa","Eskişehir","Konya","Siirt","Ankara","Kayseri"]

print(dataFrame1.Şehir)

print(dataFrame1.loc[:,"Age"])

print(dataFrame)