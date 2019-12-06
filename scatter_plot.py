# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:11:07 2019

@author: PC
"""
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("iris.csv") #dosyamı dataframeyme çevirdim
setosa=df[df.Species=="Iris-setosa"]
virginica=df[df.Species=="Iris-virginica"]
versicolor=df[df.Species=="Iris-versicolor"]

plt.scatter(setosa.PetalLengthCm,setosa.PetalWidthCm,color="pink",label="setosa")

plt.scatter(virginica.PetalLengthCm,virginica.PetalWidthCm,color="blue",label="virginica")


plt.scatter(versicolor.PetalLengthCm,versicolor.PetalWidthCm,color="orange",label="versicolor")


