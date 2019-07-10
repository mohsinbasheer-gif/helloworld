# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:38:11 2019

@author: HP
"""

print("input number:")
n=(input())
v=int(len(n))
sum=0
for i in range(v):
    sum=int(n[i])+sum    
    
print(sum)