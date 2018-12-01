# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 13:08:07 2018

@author: Urchaug
"""

#PYTHON PROGRAM TO FIND THE AREA OF A TRIANGLE
#THREE SIDES OF THE TRIANGLE
#A,B,C ARE PROVIDED BY THE USER


a = float(input('enter first side: '))
b = float(input('enter second side:'))
c = float(input('enter third side:'))

# calculate the semi-perimeter

s = (a + b + c)/2
# calculate the area
area = (s*(s-a)*(s-b)*(s-c))**0.5

print('the area of the triangle is %0.2fcm^2' %area )
