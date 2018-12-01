# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 00:42:30 2018

@author: Urchaug
"""

#acquire a number from the user and print its absolute value
n=eval(input('ener a number: '))
print('|',n,'|=',(-n if n < 0 else n),sep='')
