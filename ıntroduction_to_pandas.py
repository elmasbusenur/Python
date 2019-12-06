# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 17:51:04 2019

@author: PC
"""

import pandas as pd
dictionary={"Name":["Ali","Buse","Selma","Hakan","Bülent","Yağmur","Ahmet"],
            "Age":["18","45","12","36","40","18","63"],
            "Maas":["100","200","400","500","740","963","123"]}

dataframe1=pd.DataFrame(dictionary) #excel gibi tablo oluşturur
head=dataframe1.head() ##ilk 5 indisi verir

tail=dataframe1.tail()