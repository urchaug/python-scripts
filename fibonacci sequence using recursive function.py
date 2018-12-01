# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:50:03 2018

@author: Urchaug
"""

#python program to display the fibonacci sequence up to n-th term
#using recursive functions
def recur_fibo(n):
    """recursive function to
    print fibonacci sequence"""
    if n <=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
    #take input from the user
nterms = int(input("How many terms?"))

    #check if the number of terms is valid
if nterms <=0:
    print("please enter a positive integer")
    
else:
        
            
        print("fibonacci sequence:")
        
             
        for i in range(nterms):
            
                    
            print(recur_fibo(i))
            
            
            
    