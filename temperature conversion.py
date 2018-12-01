# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 17:49:00 2018

@author: Urchaug
"""

#converts degrees fahrenheit to degree celcius
#based on the above formula c=5/9*(f-32)
#prompt user for temperature to convert and read the supplied value

degreesF=eval(input('enter the temperature in degreesF:')) #performs the conversion
degreesC=5/9*(degreesF-32);                                #report the result
print (degreesF,'degreesF=',degreesC,'degreesC')



