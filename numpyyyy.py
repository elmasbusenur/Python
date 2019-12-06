# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:21:18 2019

@author: PC
"""
import numpy as np
#%%
# numpy basics
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])  # 1*15 vector

print(array.shape) #15 e 1 lik bir vektör

a = array.reshape(4,4) #3e 5lik matriks yaptım
b=array.reshape(8,2)
print(a.shape)
print("yeni array",a)
print(a.ndim) ##dimension boyut verir

print(b.dtype.name) ##a nın datatipinin ismi nedir

print("yeni array",b)


#%%
import numpy as np
arr=np.array([1.1,8.9,4.4,2.4,5.7,3.6,5.9,4.9])

print(arr.shape)
a=arr.reshape(4,2)
print(a.dtype.name)
#%%

import numpy as np
arr=np.array(['a','b','c','d'])
print(arr)

print(arr.dtype.name)
#%%
import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])  # 1*15 vector

print(array.shape) #15 e 1 lik bir vektör

a = array.reshape(4,4) #3e 5lik matriks yaptım
b=array.reshape(8,2)
print(a.shape)
print("yeni array",a)
print(a.ndim) ##dimension boyut verir

print(b.dtype.name) ##a nın datatipinin ismi nedir

print("yeni array",b)

print("type",type(a))
print(a.size)
print(b.size)

dizi=np.array([[1,2,3,4,4],[4,3,3,6,8],[4,7,3,10,2]])

print(dizi.shape)
np.zeros((3,4))

zeros=np.zeros((3,4))
zeros[0,0]=5

print(zeros)

np.ones((3,4))

np.empty((2,3))

x=np.arange(10,20,2)

y=np.linspace(10,50,19)