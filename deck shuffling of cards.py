# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:37:23 2018

@author: Urchaug
"""

#program to shuffle a deck of card using the module and draw 5 cards
#import modules
import itertools,random
#make a deck of cards
deck = list(itertools.product(range(1,14),['spade','heart','Diamond','club']))
#shuffle the cards
random.shuffle(deck)
#draw 5 cards
print("you got:")
for i in range(5):
    print(deck[i][0],"of",deck[i][1])
    
    
    
    