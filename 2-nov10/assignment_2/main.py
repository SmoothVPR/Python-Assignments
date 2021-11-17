#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 10, 2021
Modified: November 10, 2021
"""

import math

DAY = 2
EXERCISE = 4

class CustomClass(object):
    def __init__(self, *args, **kwargs):
        self.input = ""

    def getString(self):
        self.input = input("Enter a string: ").upper()
    
    def printString(self):
        print(self.input)


def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

def exercise_4_a():
    """
    Create a list with one number, one word and one float value. Display the output of the list.
    """
    print("exercise_4_a:")

    result = [ int(0xDEADBEEF), "0xDEADBEEF", float(0xDEADBEEF) ]
    print(result)

    print("")

def exercise_4_b():
    """
    I have a nested list [1,1[1,2]]. Grab the value of 2 from the list.
    """
    print("exercise_4_b:")

    result = [ 1, 1, [ 1, 2 ] ]
    print(result[2][1])

    print("")

def exercise_4_c():
    """
    lst=['a','b','c'] What is the result of lst[1:]?
    """
    print("exercise_4_c:")

    lst = [ 'a', 'b', 'c' ]
    print(lst[1:])

    print("")

def exercise_4_d():
    """
    Create a dictionary with weekdays an keys and week index numbers as values. Assign dictionary to a variable
    """
    print("exercise_4_d:")
    
    week = { "Sunday":    0,
             "Monday":    1,
             "Tuesday":   2,
             "Wednesday": 3,
             "Thursday":  4,
             "Friday":    5,
             "Saturday":  6 }

    # Formatting
    for x, v in week.items():
        print(f"{x}:" + " " * (12 - len(f"{x}: ")) + f"{v}")

    print("")

def exercise_4_e():
    """
    D={‘k1’:[1,2,3]} what is the output of d[k1][1]
    """
    print("exercise_4_e:")

    d = { "k1": [1, 2, 3] }
    print(d["k1"][1])

    print("")

def exercise_4_f():
    """
    Can you create a list [1,[2,3]] into a tuple
    """
    print("exercise_4_f:")

    x = [ 1, [ 2, 3 ] ]

    conversion = tuple(x)
    print(conversion)

    print("")

def exercise_4_g():
    """
    With a single set function can you turn the word ‘Mississippi’ to distinct character word.
    """
    print("exercise_4_g:")

    string = "Mississipi"
    s = set(string)

    result = "".join(list(sorted(s)))
    print(result)

    print("")

def exercise_4_h():
    """
    Can you add an element ‘X’ to the above created set
    """

    string = "Mississipi"
    s = set(string)
    s.add("X")

    result = "".join(list(sorted(s)))

    print("exercise_4_h:")
    print(result)
    print("")

def exercise_4_i():
    """
    Output of set([1,1,2,3])
    """
    print("exercise_4_i:")

    s = set([ 1, 1, 2, 3 ])

    print(s)
    print("")

def question_1():
    """
    Write a program which will find all such numbers which are:
    - divisible by 7
    - not a multiple of 5
    - between 2000 and 3200
    """
    print("Question 1:")

    print([x for x in range(2000, 3201) if (x % 7 == 0) and (x % 5 != 0)])

    print("")

def question_2():
    """
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    """
    print("Question 2:")

    fast_factorial = lambda x: math.factorial(x)
    x = int(input("Enter a number: "))

    result = fast_factorial(x)
    print("factorial:", x, "=", result)

    print("")

def question_3():
    """
    With a given integral number n, write a program to generate a dictionary that
    contains (i, i*i) such that is an integral number between 1 and n (both included).
    """
    print("Question 3:")

    x = int(input("Enter a number:"))
    d = {}

    for i in range(1, x + 1):
        d[i] = i*i
    print(d)

    print("")

def question_4():
    """
    Write a program which accepts a sequence of comma-separated numbers
    from console and generate a list and a tuple which contains every number.
    """
    print("Question 4:")

    arr = tuple(map(int, input("Enter a list of comma separated numbers: ").split(",")))
    print(arr)

    print("")

def question_5():
    """
    Define a class which has at least two methods:
    getString: to get a string from console input
    printString: to print the string in upper case.
    Also please include simple test function to test the class methods.
    """
    print("Question 5:")

    obj = CustomClass()

    obj.getString()
    obj.printString()

    print("")

if __name__ == "__main__":
    display_assignment()
    
    exercise_4_a()
    exercise_4_b()
    exercise_4_c()
    exercise_4_d()
    exercise_4_e()
    exercise_4_f()
    exercise_4_g()
    exercise_4_h()
    exercise_4_i()

    question_1()
    question_2()
    question_3()
    question_4()
    question_5()
