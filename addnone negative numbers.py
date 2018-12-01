# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:43:03 2018

@author: Urchaug
"""

entry=0
sum=0




print("enter numbers to sum,negative number ends list:")



while entry >= 0:
    
    entry=eval(input('please enter numbers to sum: '))
    if entry >= 0: 
       sum+= entry

print("sum =",sum)
        