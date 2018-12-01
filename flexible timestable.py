# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 09:38:16 2018

@author: Urchaug
"""

# print a MAX X MAX multiplication table
MAX = 10
# first ,print heading
print (end="             ")
for column in range(1, MAX + 1):
    print(end=" %2i " % column)
print()  #  go down to the next line


#  print line separator; a  portion for each column
print (end="      +")
for column in range(1,   MAX + 1) :
    print(end="_______")  # print portion of line 
print ()  # go down to the next line


# print table contents
for row in range(1, MAX + 1):      #1 <=row <= MAX,table has MAX rows
    print(end="%2i | " % row)      #print heading for this row.
    for column in range(1, MAX + 1):  #table has 10 columns.
        product= row*column;           #compute product
        print(end="%3i " % product)     #display product
    print()                              #move cursor to the next row
    
    