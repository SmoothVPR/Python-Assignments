#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 10, 2021
Modified: November 10, 2021
"""

import math

ASSIGNMENT = 2

def display_assignment():
    print( "#################")
    print(f"# Assignment: {ASSIGNMENT} #")
    print( "#################")
    print("")

def exercise_2_a():
    print("exercise_2_a")
    print(50 + 50, 100 - 10)
    print("")

def exercise_2_b():
    print("exercise_2_b")
    print("30+6, 6^6, 6**6, 6+6+6+6+6+6")
    print(30+6, 6^6, 6**6, 6+6+6+6+6+6)
    print("")

def exercise_2_c():
    print("exercise_2_c")
    print("Hello World")
    print("Hello World : 10")
    print("")

def exercise_2_d():
    """
    Input data contains values for loan size P, 
    interest rate R and length of
    time to pay out L in months.
    
    Answer should contain the required monthly payment 
    M rounded up to whole dollars (i.e. if you get non-integer result,
    increase it to nearest integer which is greater).
    """

    loan, rate, term = tuple(map(int, input("Enter loan amount, interest rate, repayment term: ").split()))
    rate /= 100 * 12 # converted to percentage and split by months in year

    monthly_payment = loan * (rate * ((1 + rate) ** term)) / ((1 + rate) ** term - 1)

    print(f"required monthly payment: {math.ceil((monthly_payment))}")

if __name__ == "__main__":
    display_assignment()
    
    exercise_2_a()
    exercise_2_b()
    exercise_2_c()
    exercise_2_d() # mortgage
