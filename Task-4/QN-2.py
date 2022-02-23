# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 13:56:58 2022

@author: ARCHANAA N
"""
# QN-2
# Write a program to accept a string from the user and display characters, 
# that are present at an even index number.
# read a string

str = input("Enter a string whose even index characters has to be displayed \n")
# create a string with characters at multiples of 2
modified_string = str[::2]
print(modified_string)