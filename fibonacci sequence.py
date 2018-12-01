# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:51:51 2018

@author: Urchaug
"""

nterms = int(input("how many terms?"))
n1=0
n2=1
count = 2
if nterms <=0:
    print("please enter a positive integer")
elif nterms == 1:
    print("fibonacci sequence:")
    print(n1)
else:
    print("fibonacci sequence:")
    print(n1,",",n2,end=',')
    while count<nterms:
        nth = n1 + n2
        print(nth,end=',')
        n1 = n2
        n2 = nth
        count += 1
        
    