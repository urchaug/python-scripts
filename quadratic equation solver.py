# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:48:31 2018

@author: Urchaug
"""

#solve the quadratic equation
#ax**2 + bx +c = 0
#a,b,c are provided by the user
#import complex math module
import cmath
a=float(input('Enter a:'))
b=float(input('Enter b:'))
c=float(input('Enter c:'))
#calculate the discriminant
d = (b**2)-(4*a*c)
#find the solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))



