# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 14:17:20 2018

@author: Urchaug
"""

#python program to find the multiplication table(from 1 to 10)c of a number input by the user
#take input from the user
num = int(input("Display multiplication table of?"))
#use for loop to iterate 10 times
for i in range(1,11):
    print(num,"x",i,'=',num*i)
    