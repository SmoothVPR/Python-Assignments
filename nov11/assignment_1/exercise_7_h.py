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
    """
    Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
    Note : Use 'continue' statement. 
    Expected Output : 0 1 2 4 5 
    """
    print("Exercise_7_h")

    for i in range(0, 6):
        if i == 3:
            continue
        print(i, end=" ")
    print("")

if __name__ == "__main__":
    display_assignment()

    main()
