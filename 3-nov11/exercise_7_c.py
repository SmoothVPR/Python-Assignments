#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 10, 2021
Modified: November 11, 2021
"""

from random import randint

DAY = 3
EXERCISE = 7

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

def main():
    print("Exercise_7_c")

    guessed = False

    answer = randint(1, 9)
    print("Guess a number between 1 and 9 (inclusive)")
    while not guessed:
        try:
            guess = int(input())
            if guess == answer:
                print("Well guessed!")
                guessed = True
            else:
                print("Nope. Guess again")
        except:
            print("Please enter a number...")

if __name__ == "__main__":
    display_assignment()
    main()
