#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 10, 2021
Modified: November 11, 2021
"""

DAY = 3
EXERCISE = 7

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

def main():
    print("Exercise_7_a")

    x = [x for x in range(1500, 2701) if (x % 7 == 0) and (x % 5 == 0)]
    print(x)

if __name__ == "__main__":
    display_assignment()
    main()
