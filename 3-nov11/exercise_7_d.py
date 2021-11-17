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
    print("Exercise_7_d")

    i = 1
    ascending = True
    for _ in range(9):
        if i == 5:
            ascending = False

        print('* ' * i)

        if ascending:
            i += 1
        else:
            i -= 1

if __name__ == "__main__":
    display_assignment()

    main()
