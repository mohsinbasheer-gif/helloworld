# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 22:16:43 2019

@author: HP
"""
#12/04/2019
date=input()
date2=input()
dcount=abs(int(date2[0]+date2[1])-int(date[0]+date[1]))
mcount=abs(int(date2[3]+date2[4])-int(date[3]+date[4]))
ycount=abs(int(date2[6]+date2[7]+date2[8]+date2[9])-int(date[6]+date[7]+date[8]+date[9]))

if(mcount==0 and ycount==0):
    print(dcount)
    
if(mcount!=0 and ycount==0):
    for i in range(abs(int(date2[3]+date2[4])),abs(int(date[3]+date[4])),-1):
        if(int(date2[3]+date2[4])==4 or int(date2[3]+date2[4])==6 or int(date2[3]+date2[4])==9 or int(date2[3]+date2[4])==11):
            dcount=dcount+30
        elif(int(date2[3]+date2[4])==2):
            dcount=dcount+28
        else:
            dcount=dcount+31
    print(dcount) 

if(mcount!=0 and ycount!=0):
    for i in range(int(date2[3]+date2[4]),int(date[3]+date[4]),-1):
            if(int(date2[3]+date2[4])==4 or int(date2[3]+date2[4])==6 or int(date2[3]+date2[4])==9 or int(date2[3]+date2[4])==11):
                dcount=dcount+30
            if(int(date2[3]+date2[4])==2):
                dcount=dcount+28
            else:
                dcount=dcount+31 
    for i in range(ycount):
            dcount=dcount+365
    print(dcount)

if(mcount==0 and ycount!=0):
    for i in range(ycount):
        dcount=dcount+365
    print(dcount)