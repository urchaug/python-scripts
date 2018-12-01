# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 21:57:54 2018

@author: Urchaug
"""

from random import randrange

def permute(lst):
    n = len(lst)
    for i in range(n - 1):
        pos = randrange(i, n)
        lst[i], lst[pos] = lst[pos], lst[i]
        
def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8]
    print('before:', a)
    permute(a)
    
    print('after :', a)
    
main()
