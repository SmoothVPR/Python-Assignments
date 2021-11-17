#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 10, 2021
Modified: November 11, 2021
"""

import sys

DAY = 3
EXERCISE = 7

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

def __usage_error():
    print( "Usage error.\n"
           "\n"
           "Example: \n"
           f"  Enter a comma separated list of numbers: 80, 22, 11, 11, 42, 5231, 612" )
    sys.exit(1)

def main():
    print("Exercise_7_f")

    try:
        x = tuple(map(int, input("Enter a comma seperated list of numbers: ").split(",")))
    except:
        __usage_error()

    get_evens = lambda x: len([x for x in x if x % 2 == 0])
    get_odds  = lambda x: len([x for x in x if x % 2 == 1])
    
    print("Number of even numbers:", get_evens(x))
    print("Number of odd numbers:", get_odds(x))

if __name__ == "__main__":
    display_assignment()

    main()
