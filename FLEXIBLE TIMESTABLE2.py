# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 20:50:58 2018

@author: Urchaug
"""

MAX=18

MAX=eval(input("please enter a number: "))




    
print(end="        ")
for column in range (1, MAX + 1):
    print(end= "%2i "  % column)
print()
print(end="    +")
for column in range( 1, MAX + 1 ):
    print(end="____")
print()
for row in range( 1, MAX + 1 ):
    print(end=   "%2i | "    %    row)
    for column in range (  1, MAX + 1):
        product = row*column;
        print (end= "%3i " % product )
    print()
