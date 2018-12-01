# -*- coding: utf-8 -*-
"""
Created on Tue May  1 20:59:24 2018

@author: Urchaug
"""

#   Factorial(n)
#      computes n!
#     returns the factorial of n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def main():
    # try out the factorial function
    print(" 0! = ", factorial(0))
    print(" 1! = ", factorial(1))
    print(" 6! = ", factorial(6))
    print(" 10! = ", factorial(10))
    
main()
