# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:42:46 2022

@author: ARCHANAA N
"""
# Question-1

# Consider the vector [10, 11, 12, 13, 14], how to build a new vector
# with 5 consecutive zeros interleaved between each value?

import numpy as np
a = int(input("Enter the first number:"))
b = int(input("Enter the first number:"))
c = b + 1
nums = np.arange(a,c)
print("Original array:")
print(nums)
w = 5
new_nums = np.zeros(len(nums) + (len(nums)-1)*(w))
new_nums[::w+1] = nums
print("\nNew array:")
print(new_nums)