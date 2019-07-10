# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 22:56:16 2019

@author: HP
"""

numb = int(input())
binary = '' 

while(numb):
 if(numb % 2 == 0):
  binary += '0'
 else:
  binary += '1'
 numb = numb//2

''.join(binary)
print(binary)
    

    