# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:30:42 2018

@author: Urchaug
"""

#program to check if a number provided by the user is an armstrong number or not
# take input from the user

num = int(input("enter a number:"))
# initialise sum
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp//= 10
    #display the result
if num == sum:
    print(num,"is an armstrong numbers")
else:
    print(num,"is not an armstrong number")
    
    
    