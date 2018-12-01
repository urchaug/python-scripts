# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 21:41:04 2018

@author: Urchaug
"""

print("help!  my computer doesn't work!")
done= False
while not done:
    print("does the computer make any sounds (fans,etc.)")
    choice=input("or show any lights? (y/n): ")
    if choice == 'n':
        choice = input("is it plugged in? (y/n): ")
        if choice == 'n':
            print("plug it in.")
        else:
            choice=input("is the switch in the \"on\" position? (y/n): ")
            if choice == 'n':
                print("turn it on.")
            else:
                choice=input("does the computer have a fuse? (y/n):")
                if choice =='n':
                    choice =input("is the outlet ok? (y/n): ")
                    if choice=='n':
                        print("check the outlet's circuit")
                        print("breaker or fuse. move to a")
                        print("new outlet,if necessary. ")
                    else:
                        print("please consult a service technician.")
                        done = True
                        
    else:
                        print("check the fuse . replace if ")
                        print("necessary")
else:

            print("please consult a service technician.")
            done = True
            
            
