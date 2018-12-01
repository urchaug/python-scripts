# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 22:15:33 2018

@author: Urchaug
"""

#python program to check if the input year is a leap year or not
year = int(input("enter a year:"))
if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            print("{0} is  a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is  a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))