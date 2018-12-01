# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 21:22:20 2018

@author: Urchaug
"""

from random import randrange

# roll the die three times
#for i in range(0, 3):
    # generate random number in the range 1 ....6
    #value = randrange(1, 6)
def show_die(spots):
    #  show the die
    print("+-----------+")
    if spots == 1:
        print("|           |")
        print("|     *     |")
        print("|           |")
    elif spots == 2:
        print("|*          |")
        print("|           |")
        print("|          *|")
    elif spots == 3:
        print("|         * |")
        print("|     *     |")
        print("| *         |")
    elif spots == 4:
        print("| *       * |")
        print("|           |")
        print("| *       * |")
    elif spots == 5:
        print("| *        *|")
        print("|      *    |")
        print("| *        *|")
    elif spots == 6:
        print("| *   *   * |")
        print("|           |")
        print("| *   *   * |")
    else:
        print("  *** Error: illegal die value *****")
    print("+-----------+")
    
# roll
# returns pseudorandom number in the range 1....6
def roll():
    return randrange(1, 6)
#   main
# simulates the roll of a die three times
def main():
    #  roll the die three times
    for i in range(0, 3):
        show_die(roll())
main()  # run the program
    