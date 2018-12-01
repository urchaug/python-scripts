# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:46:58 2018

@author: Urchaug
"""

#PYTHON PROGRAM TO CHECK IF THE INPUT NUMBER IS A PRIME OR NOT
# TAKE INPUT FROM THE USER
num = int(input("enter a number:"))
#prime numbers are greater than 1
if num > 1:
    #check for factors
    for i in range(2,num):
        if (num%i) == 0:
            
          print(num,"is not a prime number")
          print(i,"times",num//i,"is",num)
          break
    else:
        
        print(num,"is a prime number")
#if input number is less than or equal to 1,it is not a prime 
else:
    print(num,"is not a prime number")
    
    