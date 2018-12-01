# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:06:15 2018

@author: Urchaug
"""

# python program to convert decimal number into binary,octal and hexadecimal number system
# take decimal number from user
dec = int(input("Enter an integer:"))
print("the decimal value of",dec,"is")
print(bin(dec),"in binary.")
print(oct(dec),"in octal.")
print(hex(dec),"in hexadecimal.")
