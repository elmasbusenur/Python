# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 10:39:55 2019

@author: PC
"""

import pandas as pd
dictionary={"Name":["Ali","Buse","Selma","Hakan","Bülent","Yağmur","Ahmet"],
            "Age":[18,45,12,36,40,18,63],
            "Maas":[100,200,400,500,740,963,123]}

dataFrame1=pd.DataFrame(dictionary) #excel gibi tablo oluşturur
head=dataFrame1.head() ##ilk 5 indisi verir

tail=dataFrame1.tail()

print(dataFrame1.columns)

print(dataFrame1.info())

print(dataFrame1.dtypes)

print(dataFrame1.describe())