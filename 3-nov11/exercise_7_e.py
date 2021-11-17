#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 11, 2021
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
    print("Exercise_7_d")

    print("Reversed string:", input("Enter a string: ")[::-1].lstrip())

if __name__ == "__main__":
    display_assignment()

    main()
