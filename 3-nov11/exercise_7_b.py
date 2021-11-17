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
           f"  {sys.argv[0]} 80" )
    sys.exit(1)

def main():
    if len(sys.argv) != 2:
        __usage_error()

    print("Exercise_7_b")

    try:
        x = int(sys.argv[1])
    except:
        __usage_error()

    to_f = lambda x: (x * 9 / 5) + 32
    to_c = lambda x: (x - 32) * (5 / 9)

    assert to_c(140) == 60.00
    assert to_c(212) == 100.00
    assert to_f(0)   == 32.00
    assert to_f(60)  == 140.00

    print(f"{x} Celsius is {to_f(x):.2f} in Fahrenheit")
    print(f"{x} Fahrenheit is {to_c(x):.2f} in Celsius")

if __name__ == "__main__":
    display_assignment()
    main()
