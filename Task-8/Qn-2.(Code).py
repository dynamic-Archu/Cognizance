# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 23:30:06 2022

@author: ARCHANAA N
"""

# Question-2

# Consider two random array A anb B, check if they are equal

import numpy as np
print()
print("Enter no. of elements in array 1:")
n = int(input())
print()
print("Enter inputs for array 1:")
arr1 = input()
a = list(map(int,arr1.split(' ')))
print()
print("First array:")
print()
print(a)
print()
print("Enter no. of elements in array 2:")
m = int(input())
print()
print("Enter inputs for array 2:")
arr2 = input()
b = list(map(int,arr2.split(' ')))
print()
print("Second array:")
print()
print(b)
print()
print("Check both the user given arrays whether they are equal or not!")
print("If equal, print true and if not, print false")
print()
array_equal = np.allclose(a, b)
print(array_equal)