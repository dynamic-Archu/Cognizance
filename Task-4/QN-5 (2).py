# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:37:23 2022

@author: ARCHANAA N
"""

# QN-5
# Print the following pattern.

n = int(input("Enter the number of rows of stars that needs to be printed:"))
for i in range(n) :
    for j in range(n-i-1) :
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()