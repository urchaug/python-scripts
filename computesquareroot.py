# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:41:04 2018

@author: Urchaug
"""

#  file compute squareroot.py
# get value from the user
val=eval(input('enter number: '))
# computes a provisional sqaure root
root = 1.0;
#how far off is our provisional root?
diff=root*root-val
#loop until the provisional root
#is close enough to the actual root
while diff> 0.00000001 or diff < -0.00000001:
    root=(root + val/root)/2        #computes new provisional root
    print(root, 'squared is ',root*root)  #reports how we are doing 
    #how bad is our current approximation?
    diff=root*root - val
    #reports approximate square root
print('square root of',val,"=",root)
