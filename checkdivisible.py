# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 20:53:04 2019

@author: HP
"""
print("enter numerator")
numerator=int(input())
print("enter denominator")
denominator=int(input())

if (numerator%denominator==0 ):
    print("number",numerator,"is completely divisible by",denominator)
    
if (numerator%denominator!=0 ):
    print("number",numerator,"is not completely divisible by",denominator)