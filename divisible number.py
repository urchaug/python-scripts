# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 11:14:33 2018

@author: Urchaug
"""

#python program to find numbers divisible by thirteen
#from a list using anonymous function
#take a list of numbers
my_list = [12,65,54,39,102,339,221,]
#use anonymous function to filter
result = list(filter(lambda x:(x%2 == 0),my_list))
#display the result
print("numbers divisible by 2 are",result)
