# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 21:32:13 2019

@author: PC
"""

import numpy as np

import pandas as pd
dictionary={"Name":["Ali","Buse","Selma","Hakan","Bülent","Yağmur","Ahmet"],
            "Age":[18,45,12,36,40,18,63],
            "Maas":[100,200,400,500,740,963,123]}

dataFrame1=pd.DataFrame(dictionary)
dataFrame1["Şehir"]=["İstanbul","Bursa","Eskişehir","Konya","Siirt","Ankara","Kayseri"]
dataFrame1["yeni_feature"]=[7,4,9,1,15,5,3]

dataFrame1["list_comp"]=[each*2 for each in dataFrame1.Age ] ##dataframe1 age al 2 ile çarp list_comp oluştur içine yaz

def multiply(Age):
    return Age*2

dataFrame1["apply_metodu"]=dataFrame1.Age.apply(multiply)