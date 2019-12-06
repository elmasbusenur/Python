# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 15:48:21 2019

@author: PC
"""
import numpy as np

import pandas as pd
dictionary={"Name":["Ali","Buse","Selma","Hakan","Bülent","Yağmur","Ahmet"],
            "Age":[18,45,12,36,40,18,63],
            "Maas":[100,200,400,500,740,963,123]}

dataFrame1=pd.DataFrame(dictionary)
dataFrame1["Şehir"]=["İstanbul","Bursa","Eskişehir","Konya","Siirt","Ankara","Kayseri"]

import numpy as np
ortalama_maas=np.mean(dataFrame1.Maas)

dataFrame1["maas_seviyesi"]=["Düşük" if ortalama_maas> each else "Yüksek" for each in dataFrame1.Maas]

for each in dataFrame1.Maas:
    print(each)
    
dataFrame1["yeni feature"]=[7,4,9,1,15,5,3]


dataFrame1.columns = [each.split()[0]+"_"+each.split()[1] if(len(each.split())>1) else each for each in dataFrame1.columns]
