# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 17:43:41 2019

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


dataFrame1.drop(["yeni_feature"], axis=1,inplace=True)
data1=dataFrame1.head()
data2=dataFrame1.tail()

data_concat=pd.concat([data1,data2], axis=0)

Maas=dataFrame1.Maas
Age=dataFrame1.Age

data_h_concat=pd.concat([Maas,Age],axis=1)