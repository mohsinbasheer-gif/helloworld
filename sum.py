# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:30:47 2019

@author: HP
"""

print("input number:")
n=int(input())
sum=0
for i in range(n+1):
    sum=sum+i
    
print("Sum of n Positive integers till", n," is", sum)