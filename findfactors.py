# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 20:37:49 2018

@author: Urchaug
"""

#list the factors of the integers 1.......MAX
MAX=20
n=1 #starts with 1
while n<=MAX:
    factor = 1
    print (end=str(n) + ':  ')
    while factor <= n:
        if n % factor == 0:
            print(factor,end= ' ')
        factor +=1
    print()
    n +=1
    