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
    Write a Python program that prints each item and its corresponding type from the following list:
    datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
    """
    print("Exercise_7_g")

    datalist = [ 1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'} ]

    for item in datalist:
        print(f"Type of {item}: {type(item)}")

if __name__ == "__main__":
    display_assignment()

    main()
