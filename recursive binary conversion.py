# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:12:49 2018

@author: Urchaug
"""

#python program to convert decimal 
#number into binary number using recursive function

def binary(n):
    """function to print number
    for the input decimal using recursion"""
    if n>1:
        binary(n//2)
    print(n%2, end="")
    
    
    #take decimal number from the user
dec = int(input("Enter an integer:"))
binary(dec)
  