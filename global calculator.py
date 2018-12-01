# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 09:06:06 2018

@author: Urchaug
"""

#    Help_screen
#      displays information about how the program works
#       accepts no parameters
#     returns nothing


def help_screen():
    print("add:   adds two numbers")
    print("substract:   substracts two numbers")
    print("print:   displays the result of the latest operation")
    print("help:  displays this help screen")
    print("quit:   exits the program")
    
    
#   menu
#      display a menu
#      accepts no parameters
#      returns string entered by the user.
def menu():
    #   display a menu
    return input("=== A)   S)ubstract P)rint H)elp  Q)uit  ===")
    # global variables used by several functions
result = 0.0
arg1 = 0.0
arg2 = 0.0
 
#  get_input
#     assigns the globals arg1 and arg2 from user keyboard
#  input
def get_input():
    global arg1,arg2 #  arg1 and arg2 are globals
    arg1 = float(input("enter argument #1:  "))
    arg2 = float(input("enter argument #2:  "))
# report
    #   reports the value of the global result
def report():
    #  not assigning to result,global keyword not needed
    print(result)
def add():
    global result   #  assignment to result,global keyword needed
    result = arg1 + arg2
    
    
    
    # substract
    # assigns the difference of the globals arg1 and arg2
    # to the global variable results
def substract():
    global result   # assigning to result,global keyword needed
    result = arg1 - arg2
    
    # main
    # runs a command loop that allows users to perform simple arithmetric.
def main():
    done = False; # initially not done
    while not done:
          choice = menu()    # get user's choice
        
          if choice == "A" or choice == "a":  # addition
            get_input()
            add()
            report()
          elif choice == "S" or choice ==  "s":  # substraction
            get_input()
            substract()
            report()
          elif choice == "P" or choice == "p":  # print
            report()
          elif choice == "H" or choice == "h":  #  help
            help_screen()
          elif choice == "Q" or choice == "q": # quit
            done = True
            
            
            
main()
