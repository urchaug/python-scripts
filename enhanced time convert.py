# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 20:29:13 2018

@author: Urchaug
"""

#file enhancedtimeconv.py
#get the number of seconds
seconds=eval(input("please enter the number of seconds:"))
#first,compute the number of hours in the given number of seconds
#note:integer division with possible truncation
hours=seconds//3600 # 3600 seconds= 1 hours
#computes the remaining seconds after the hours are accounted for
seconds=seconds%3600
#next,compute the number of minutes in the remaining number of seconds
minutes=seconds//60  # 60 seconds = 1 minute
#compute the remaining seconds after the minutes are accounted for 
seconds=seconds%60
#reports the results
print(hours,":",sep="",end="")
#computes tens digit of minutes
tens=minutes//10
#computes ones digit of minutes
ones=minutes%10
print(tens,ones,":",sep="",end="")
#computes tens digit of seconds
tens=seconds//10
#computes ones digit of seconds
ones=seconds%10
print(tens,ones,sep="")
