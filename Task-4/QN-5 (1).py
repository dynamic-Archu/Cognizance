# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:46:28 2022

@author: ARCHANAA N
"""

# QN-5
# Print the following pattern.

n=int(input("Enter the number of rows:"))
for i in range(n): 
  print(" "*(n-1-i)+"* "*(i+1))