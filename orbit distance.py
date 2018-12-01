# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 12:19:55 2018

@author: Urchaug
"""

# use some functions and values from the math package
from math import sqrt, sin, cos, pi
# location of orbiting point is (x,y)
# location of fixed point is always (100, 0)
# AKA (P_X, P_Y).   change these as necessary.
p_x = 100
p_y = 0


#  radians in 10 degrees
radians = 10 * pi/180


#   precompute the cosine and sine of 10 degrees
COS10 = cos(radians)
SIN10 = sin(radians)


# get starting point from user
x, y = eval(input("enter initial satellite coordinates (x,y):"))


#  compute the initial distance
d1= sqrt((p_x - x) * (p_x - x)  +  (p_y - y) * (p_y - y))
#  let the satellite orbit 10 degrees
x_old = x;                 # REMEMBER X'S ORIGINAL VALUE
x = x*COS10 - y*SIN10      #  COMPUTES NEW X VALUE
#X'S VALUE HAS CHANGED, BUT Y'S CALCULATE DEPENDS ON
#  X'S ORIGINAL VALUE, SO USE X_OLD INSTEAD OF X.
y = x_old*SIN10 + y*COS10
#  COMPUTE THE NEW DISTANCE
d2 = sqrt((p_x - x) * (p_x - x)  + (p_y - y)*(p_y - y))
#print the difference in the distance
print("difference in distances: % .3f" % (d2 - d1))


