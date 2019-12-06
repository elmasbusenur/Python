# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:10:35 2019

@author: PC
"""
import numpy as np
a=np.array([1,2,9,6])
b=np.array([4,3,9,8])

print(a)
print(b)
print(a+b)
print(a-b)
print(a**2)

print(a<2)

a=np.array([[1,2,6],[7,8,1]])
b=np.array([[1,3,9],[7,8,2]])

print(a*b) #matris çarpımı değil
print(a.shape)

a.dot(b.T)
##a.dot(b) dersek hata verir 2x3 2x3 matris çarpılamaz

print(np.exp(a))

a=np.random.random((5,5)) #0 1 arası random sayılar oluştur

a.sum() #randomda toplama

a.max
a.min
print(a.max())
print(a.min())

print(a.sum(axis=0))  #kolonlardaki toplama

print(a.sum(axis=1)) #satırlarda toplama

np.square(a) #karesini al

np.sqrt(a)

np.add(a,a)