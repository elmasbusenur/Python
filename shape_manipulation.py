# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:38:28 2019

@author: PC
"""

import numpy as np

array=np.array([[1,2,3],[4,5,6],[7,8,9]])
a=array.ravel() #düzlüyor

array2=a.reshape(3,3)

arrayT=array2.T

print(arrayT)
print(array2)

print(a)
print("-------------------------------------------------------------------------------")

array5=np.array([[1,2],[3,4],[4,5]])

print(array5)