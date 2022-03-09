# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 00:14:28 2022

@author: ARCHANAA N
"""
# Question-4

# Convert the first character of each element in a series to uppercase?

import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
q = ""
s = ser.str.title()
i = 0
while i < len(ser):
    q = q + s[i]
    q = q + " "
    i = i + 1
print(q)