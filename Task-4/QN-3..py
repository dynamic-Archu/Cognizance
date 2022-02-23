# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:51:27 2022

@author: ARCHANAA N
"""

import pandas as pd
table = []

count = int(input(" Enter number of students whose datas has to be displayed: "))

for i in range(0, count):
    print(" Enter details of each student regarding the following in the respective order\n")
    print(" Roll.No.\n")
    print(" Name\n")
    print(" Marks\n")
    table.append([])
    for j in range(0, 4):
        if j==3:
           Enter_details = ''
        else:  
           Enter_details = input()
        table[i].append(Enter_details)

print(table)
df = pd.DataFrame(table, columns=["Roll.No.", "Name", "Marks", ""])
df = df.set_index(['Roll.No.', 'Name', 'Marks'])
print(df)
print(df[1:2])