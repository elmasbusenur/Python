# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:47:36 2019

@author: PC
"""

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv") #dosyamı dataframeyme çevirdim
setosa=df[df.Species=="Iris-setosa"]
virginica=df[df.Species=="Iris-virginica"]
versicolor=df[df.Species=="Iris-versicolor"]

plt.hist(setosa.PetalLengthCm, bins=10)

plt.xlabel("PetalLengthCm values")
plt.ylabel("frekans")
plt.title("hist")
plt.show()