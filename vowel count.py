# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:31:21 2018

@author: Urchaug
"""

#program to count the number of each vowel in a string
#string of vowels
vowels = 'aeiou'
#take input from the user
ip_str = input("Enter a string:")
# make it suitable for caseless comparisons
ip_str = ip_str.casefold()
# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
#count the vowels
for char in ip_str:
    if char in count:
        count[char] += 1
print(count)
