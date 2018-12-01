# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 22:08:34 2018

@author: Urchaug
"""

from math import sqrt

max_value = eval(input("display primes up to what value? "))
value = 2 #smallest prime number


while value <= max_value:
    #  see if value is prime
    is_prime =  True  #provisionally, value is prime
    #   try all possible factors from 2 to value -1
    trial_factor = 2
    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
            is_prime = False;      #  found a factor
            break                 #no need to continue;it is not a prime
        trial_factor += 1          # try the next potential factor
    if is_prime:
        print(value, end= ' ')     # display the prime number
    value += 1                        # try the next potential prime number
print ()                           # move the cursor down to the next line

        