# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:40:39 2018

@author: Urchaug
"""

#python program to display calendar of a given month of the year
#import module
import calendar
# ask of month and year
yy = int(input("Enter year:"))
mm = int(input("Enter month:"))
#display the calender
print(calendar.month(yy,mm))