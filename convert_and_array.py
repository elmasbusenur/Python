# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:39:48 2019

@author: PC
"""
import numpy as np

liste=[1,2,3,4]

array=np.array(liste)

liste2=list(array)

a=np.array([1,2,3,4])
b=a
c=a

c[0]=89#böyle yaparsak hepsi değişir çünkü hafızaya değer olarak depolanırlar

##nasıl düzeltilir
d=np.array([1,2,3,4])
e=d.copy()
f=d.copy()

f[0]=23
e[1]=25