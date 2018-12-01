# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:59:49 2018

@author: Urchaug
"""

#program to sort alphabetically the words
#from a string provided by the user
#take input from the user
my_str = input("enter a string:")
#breakdown the string into a list of words
words = my_str.split()
#sort the list
words.sort()
#display the sorted words
for word in words:
    print(word)
    