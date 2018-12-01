# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 10:39:53 2018

@author: Urchaug
"""

#  help_screen
#   displays information about how the program works
#   accepts no parameters
#   returns nothing
def help_screen():
    print("add:   Adds two numbers")
    print("substract:   substract two numbers")
    print("print:    displays the result of the latest operation")
    print("help:     displays this help screen")
    print("quit:      exits the program")
#  menu
#  display a menu
#  accepts no parameters
#  returns the string entered by the user.
def menu():
    #  display a menu
    return input("=== A)dd S)ubtract P)rint H)elp Q)uit ===")

    
#    main 
#      runs a command loop that allows users to 
#      performs simple arithmetic.
def main():
    result = 0.0
    done = False;  #  initially not done
    while not done:
        choice = menu()   # get user's choice
        
        if choice == "A" or choice == "a":   #  addition
            arg1 = float(input("enter arg1: "))
            arg2 = float(input("enter arg2: "))
            result = arg1 + arg2
            print(result)
        elif choice == "S" or choice == "s":  # substraction
            
            arg1 = float(input("enter arg1: "))
            arg2 = float(input("enter arg2: "))
            result = arg1 - arg2
            print(result)
        elif choice == "P" or choice == "p": #  print
            print(result)
        elif choice == "H" or choice == "h": #  help
            help_screen()
        elif choice == "Q" or choice == "q":  # quit
            done = True
            
            
main()


            