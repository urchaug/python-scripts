# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 18:23:32 2018

@author: Urchaug
"""

#file timeconv.py
seconds=eval(input("please enter the number of seconds:")) #get the number of seconds

#first,compute the number of hours in the given number of seconds
#note:integer division with possible truncation
hours=seconds//3600 #3600 seconds = 1hours
#compute the remaining seconds after the hours are accounted for
seconds=seconds%3600
#next,compute the number of minutes in the remaining number of seconds
minutes=seconds//60 #60 seconds = 1 minute
# compute the remaining seconds after the minutes are accounted for
seconds = seconds%60
print(hours,"hr,",minutes,"min,",seconds,"sec")  #report the results


                    