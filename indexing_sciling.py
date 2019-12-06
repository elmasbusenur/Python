# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:09:21 2019

@author: PC
"""

import numpy as np

array=np.array([1,2,3,4,5,6,7])

print(array[0])

print(array[0:3])

##ters çevirme
reverse_array=array[::-1]
print(reverse_array)

array1=np.array([[1,2,3,4,5,6],[7,8,1,2,9,3]])
print(array1)

print(array1[1,1])
print(array1[:,1])

print(array1[1,1:4]) #1.satır 1 2 3. sutunlar

print(array1[-1,:])

print(array1[:,-1])