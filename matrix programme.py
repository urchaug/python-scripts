# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 21:55:34 2018

@author: Urchaug
"""

#PROGRAM TO ADD TWO MATRICES
#USING NESTED LOOP


x = [[5,8,1],
     [6,7,3],
     [4,5,9]]


y = [[12,7,3],
     [4,5,6],
     [7,8,9]]


result = [[0,0,0],
          [0,0,0],
          [0,0,0]]


#iterate through rows
for i in range(len(x)):
    #iterate through columns
  for j in range(len(x[0])):
        result[i][j] = x[i][j] + y[i][j]
for r in result:
   print(r)
            
          