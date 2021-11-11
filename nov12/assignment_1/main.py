#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 11, 2021
Modified: November 11, 2021
"""

# import math

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
    - [ ] Define a function func3(x,y,z) that takes three arguments x,y,z where z is
          true it will return x and when z is false it should return y . func3(‘hello’goodbye’,false)
    """
    print("exercise_8_3:")

    if z:
        return x
    else:
        return y

def func4(x, y):
    """
    define a function func4(x,y) which returns the product of both the values.
    """
    print("exercise_8_4:")

    print(x, "*", y, "= ", end="")
    return x * y


def is_even(x): # exercise_8_5
    """
    D={‘k1’:[1,2,3]} what is the output of d[k1][1]
    """
    print("exercise_8_5:")

    return x % 2 == 0

def exercise_8_6():
    """
    Can you create a list [1,[2,3]] into a tuple
    """
    print("exercise_8_6:")

    x = [ 1, [ 2, 3 ] ]

    conversion = tuple(x)
    print(conversion)

    print("")

def exercise_8_7():
    """
    With a single set function can you turn the word ‘Mississippi’ to distinct character word.
    """
    print("exercise_8_7:")

    string = "Mississipi"
    s = set(string)

    result = "".join(list(sorted(s)))
    print(result)

    print("")

def exercise_8_8():
    """
    Can you add an element ‘X’ to the above created set
    """
    print("exercise_8_8:")

    string = "Mississipi"
    s = set(string)
    s.add("X")

    result = "".join(list(sorted(s)))

    print("exercise_8_h:")
    print(result)
    print("")

def exercise_8_9():
    """
    Output of set([1,1,2,3])
    """
    print("exercise_8_9:")

    s = set([ 1, 1, 2, 3 ])

    print(s)
    print("")

def exercise_8_10():
    """
    Output of set([1,1,2,3])
    """
    print("exercise_8_10:")

    s = set([ 1, 1, 2, 3 ])

    print(s)
    print("")

def exercise_8_11():
    """
    Output of set([1,1,2,3])
    """
    print("exercise_8_11:")

    s = set([ 1, 1, 2, 3 ])

    print(s)
    print("")

def exercise_8_12():
    """
    Output of set([1,1,2,3])
    """
    print("exercise_8_12:")

    s = set([ 1, 1, 2, 3 ])

    print(s)
    print("")

def exercise_8_13():
    """
    Output of set([1,1,2,3])
    """
    print("exercise_8_13:")

    s = set([ 1, 1, 2, 3 ])

    print(s)
    print("")

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
    # exercise_8_7()
    # exercise_8_8()
    # exercise_8_9()
    # exercise_8_10()
    # exercise_8_11()
    # exercise_8_12()
    # exercise_8_13()
