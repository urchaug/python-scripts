# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 21:41:17 2018

@author: Urchaug
"""

#program to multiply two matrices
#using nested loops
#3x3 matrix
x = [[12,7,3],
     [4,5,6],
     [7,8,9]]
#3x4 matrix
y = [[5,8,1,2],
     [6,7,3,0],
     [4,5,9,1]]
#result is 3x4
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
#iterate through rows of x
for i in range(len(x)):
    #iterate through columns of y
    for j in range(len(y[0])):
        #iterate through rows of y
        for k in range(len(y)):
            result[i][j] += x[i][k]*y[k][j]
for r in result:
    print(r)
    



