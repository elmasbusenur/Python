# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:09:02 2019

@author: PC
"""

import pandas as pd

df=pd.read_csv("iris.csv")

print(df.columns)

print(df.Species.unique()) #benzersiz kolonları yazdırma

print(df.info()) # colonların içerik bilgisini verir.Örn;float dan 4 adet int 1 adet nesne 1 adet gibi

print(df.describe())#string olmayan numerik değerleri kıyaslamamızı sağlar

setosa=df[df.Species=="Iris-setosa"] #dataframe türleri var bu türleri dataframeden çek setosaya eşitle
versicolor=df[df.Species=="Iris-versicolor"]
print(setosa.describe()) #anlamlı datalar elde edip karşılaştırma yapılabilir
print(versicolor.describe())