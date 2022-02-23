# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 13:08:41 2022

@author: ARCHANAA N
"""
# QN-4
# Write a program to check if the given number is a palindrome number.

n=int(input("Enter the number that has to be checked whether it is a palindrome number or not: "))
temp=n
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")