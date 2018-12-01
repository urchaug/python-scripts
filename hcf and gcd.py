# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 10:18:52 2018

@author: Urchaug
"""

#python program to find the HCF of two input number
#define a function
def hcf(x,y):
    
    """this function takes two integers
    and returns the HCF"""
    # choose the smaller number
    if x>y:
    
       smaller = y
    else:
       smaller = x
    for i in range(1,smaller + 1):
        if((x%i==0) and (y%i==0)):
            
            hcf = i
            
            
    return hcf

#take input from user
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
print("The H.C.F. of",num1,"and",num2,"is",hcf(num1,num2))



            