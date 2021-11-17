#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 11, 2021
Modified: November 11, 2021
"""

import math

DAY = 4
EXERCISE = 8

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

def func(): # exercise_8_1
    """
    - [x] Create a function func() which prints a text 'Hello World'
    """
    print("exercise_8_1:")

    print("Hello World")

    print("")

def func1(name): # exercise_8_2
    """
    - [x] Create a function which func1(name)  which takes a value name
          and prints the output 'Hi My name is Google'
    """
    print("exercise_8_2:")

    print(f"Hi, My name is {name}")

    print("")

def func3(x, y, z):
    """
    - [x] Define a function func3(x,y,z) that takes three arguments x,y,z where z is
          true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)
    """
    print("exercise_8_3:")

    if z:
        return x
    else:
        return y

def func4(x, y):
    """
    - [x] define a function func4(x,y) which returns the product of both the values.
    """
    print("exercise_8_4:")

    print(x, "*", y, "= ", end="")
    return x * y

def is_even(x): # exercise_8_5
    """
    define a function called as is_even that takes one argument,
    which returns true when even values is passed and false if it is not.
    """
    print("exercise_8_5:")

    return x % 2 == 0

def is_greater(a, b):
    """
    define a function that takes two arguments, and returns true if the first
    value is greater than the second value and returns false if it is less than
    or equal to the second.
    """
    print("exercise_8_6:")

    return a > b

def sum_of_two(a, b):
    """
    Define a function which takes arbitrary number of arguments and returns the sum of the arguments.
    """
    print("exercise_8_7:")

    return a + b

def n_args_to_list(*args):
    """
    Define a function which takes arbitrary number of arguments and
    returns a list containing only the arguments that are even.
    """
    print("exercise_8_8:")

    return [int(x) for x in list(args) if int(x) % 2 == 0]

def format_str(string):
    """
    Define a function that takes a string and returns a matching string
    where every even letter is uppercase and every odd letter is lowercase 
    """
    print("exercise_8_9:")

    return "".join([x.lower() if i % 2 == 0 else x.upper() for i, x in enumerate(string)])

def greater_or_lesser(a, b):
    """
    Write a function which gives lesser than a given number
    if both the numbers are even, but returns greater if one or both or odd.
    """
    print("exercise_8_10:")

    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        else:
            return b
    else:
        if a > b:
            return a
        else:
            return b

def same_letter(string_1, string_2):
    """
    Write a function which takes two-strings and returns true if
    both the strings start with the same letter
    """
    print("exercise_8_11:")

    return string_1[0] == string_2[0]

def opposite_distance(x):
    """
    Given a value, return a value which is twice as far as other side of 7
    """
    print("exercise_8_12:")

    result = 7

    if x > 7:
        result -= (math.fabs(x - 7) * 2)
    else:
        result += (math.fabs(x - 7) * 2)

    return result

def special_formatter(string):
    """
    A function that capitalizes first and fourth character of a word in a string.
    """
    print("exercise_8_13:")

    return "".join([x.upper() if i == 0 or i == 3 else x for i, x in enumerate(string)])

if __name__ == "__main__":
    display_assignment()
    
    # exercise_8_1
    func()

    # exercise_8_2
    func1("Malik")

    # exercise_8_3
    print(func3("hello", "goodbye", False), "\n")
    print(func3("hello", "goodbye", True),  "\n")

    # exercise_8_4
    print(func4(20, 5), "\n")

    # exercise_8_5
    print(is_even(22), "\n")
    print(is_even(21), "\n")

    # exercise_8_6()
    print("5 > 4 ?", is_greater(5, 4), "\n")
    print("4 > 5 ?", is_greater(4, 5), "\n")

    # exercise_8_7()
    print("420 + 69 =", sum_of_two(420, 69), "\n")

    # exercise_8_8()
    print("list of 10 args:", n_args_to_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), "\n")

    # exercise_8_9()
    print("test string:", format_str("test string"), "\n")

    # exercise_8_10()
    print("8, 10:", greater_or_lesser(8, 10), "\n")
    print("9, 10:", greater_or_lesser(9, 10), "\n")

    # exercise_8_11()
    print("Freaky, Friday:", same_letter("Freaky", "Friday"), "\n")
    print("Spooky, Friday:", same_letter("Spooky", "Friday"), "\n")

    # exercise_8_12()
    # assert opposite_distance(8) == 5
    # assert opposite_distance(6) == 9
    print("12:", opposite_distance(12), "\n")
    print("0:", opposite_distance(0), "\n")

    # exercise_8_13()
    print("captitalize this!:", special_formatter("capitalize this"), "\n")
