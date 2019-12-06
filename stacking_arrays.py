# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:34:11 2019

@author: PC
"""

import numpy as np

array1=np.array([[1,2],[3,4]])

array2=np.array([[-1,-2],[-3,-4]])

array3=np.vstack((array1,array2))

array4=np.hstack((array1,array2))

#aynı büyüklüğe sahip olmalılar array5=np.vstack((array4,array3))
