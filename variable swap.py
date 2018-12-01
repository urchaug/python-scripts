# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 17:07:33 2018

@author: Urchaug
"""

#python program to swap two variables
#provided by the user
x = input('Enter value of x:')
y = input('Enter value of y:')
#create a temporary variable and swap the values
temp = x
x = y
y = temp
print('the value of x after swaping:{}'.format(x))
print('the value of y after swaping:{}'.format(y))


