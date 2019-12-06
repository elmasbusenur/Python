# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:54:48 2019

@author: PC
"""

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_csv("iris.csv") #dosyamı dataframeyme çevirdim
setosa=df[df.Species=="Iris-setosa"]
virginica=df[df.Species=="Iris-virginica"]
versicolor=df[df.Species=="Iris-versicolor"]

df.plot(grid=True,alpha=0.9,subplots=True)

plt.show()

plt.subplot(2,1,1)

plt.plot(setosa.Id,setosa.PetalLengthCm,color="red",label="setosa")

plt.ylabel("setosa.PetalLengthCm")

plt.subplot(2,1,2)

plt.plot(versicolor.Id,versicolor.PetalLengthCm,color="green",label="versicolor")

plt.ylabel("versicolor.PetalLengthCm")

plt.show()