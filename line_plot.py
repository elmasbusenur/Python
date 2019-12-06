# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 21:02:31 2019

@author: PC
"""
#iris.csv virgülle ayrılmış değerler
#species tür demek iris bir çiçek ve virginica setosa versicolor onun türleri
#sepalLengthCm sepalWidthCm PetalLengthCm .. bunlar future 
#yukarıdaki futureler taç yaprak çanak yaprak tarı şeyler
#150 tane tür var sample var sample=satır

import matplotlib.pyplot as plt
df1=df.drop(["Id"],axis=1) #işime yaramıycak id df1 e kaydederken drop ediyorum #1 sutun 0 satır
setosa=df[df.Species=="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]

plt.plot(setosa.Id,setosa.PetalLengthCm, label="Setosa", color="red")  #import ettiğim kütüphane için olan kısltma
plt.plot(versicolor.Id,versicolor.PetalLengthCm, label="Versicolor", color="purple")  #import ettiğim kütüphane için olan kısltma
plt.plot(virginica.Id,virginica.PetalLengthCm, label="Virginica", color="orange")  #import ettiğim kütüphane için olan kısltma
plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()#----- Setosa-PetalLengthCm yazan yer
plt.show()


#df1.plot(grid=True,linestyle=":") #grid dörtgenlere ayırıyor grafiği #linestyla noktosal gösterir
df1.plot(grid=True,alpha=0.5) #alpha opasity opaklık demek

plt.show()
