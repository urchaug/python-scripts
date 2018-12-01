# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:24:49 2018

@author: Urchaug
"""

#program to convert kilometers
#into miles where input is provided by the user in kilometers
#take input from the user
kilometers = float(input("How many kilometers?:"))
#conversion factor
conv_fac = 0.621371
#calculate miles
miles = kilometers*conv_fac
print('%0.3f kilometers is equal to %0.3f miles'%(kilometers,miles))
