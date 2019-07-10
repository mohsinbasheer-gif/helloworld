# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:05:35 2019

@author: HP
"""


print("Please enter principal amount")
p=float(input())
print("Please Enter Rate of interest in %")
r=float(input())
print("Please Enter time")
t=float(input())
i=p*r*t
print("After",t," years your principal amount",p," over an interest rate of ",r,"% will be",i)