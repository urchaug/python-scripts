# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 00:15:14 2018

@author: Urchaug
"""

height = eval(input("enter the height of tree: "))
row=0
while row < height:
    count = 0
    while count < height - row:
        print(end=" ")
        count += 1
    count = 0
    while count < 1*row + 1:
        print(end="**")
        count += 1
    while count < height + row:
        print(end="  ")
        count += 1
    print()
    row += 1
    