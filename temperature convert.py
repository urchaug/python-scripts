# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 12:58:12 2018

@author: Urchaug
"""

#python program to convert temperature in celcius to fahrenheit where input is provided by the user in degree celcius
#take input from the user 
celcius = float(input("enter degree celsius:"))
# calculate fahrenheit
fahrenheit = (celcius * 1.8) + 32
print("%0.1f degree celcius is equal to %0.1f degree fahrenheit" %(celcius,fahrenheit))
