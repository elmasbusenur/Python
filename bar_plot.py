# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:51:00 2019

@author: PC
"""

import numpy as np
x=np.array([1,2,3,4,5,6,7])
a=[("istanbul","konya","kars","karabük","antalya","izmir","izmit")]
y=x*2+5

plt.bar(x,y)

plt.title("bar plot")

plt.xlabel("x")
plt.ylabel("y")

plt.show

plt.figure()