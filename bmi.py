# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:21:38 2019

@author: HP
"""

print("input height in cm:")
h=int(input())
cmm=h/100
print("input weight in kg:")
w=int(input())
res=w/(cmm*cmm)
print("your bmi is", res)