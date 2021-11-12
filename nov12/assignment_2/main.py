#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 11, 2021
Modified: November 11, 2021
"""

# import math

DAY = 4
EXERCISE = 9

data_set_1 = [ [34597, 98762, 77226, 88112],     # Order Number
               ["Learning Python, Mark Lutz",    # Book Title and Author
                "Programming Python, Mark Lutz",
                "HeadFirst Python, Paul Barry",
                "Einfuhrung in Python3, Bernd Klein"],
               [4, 5, 3, 3],                     # Quantity
               [40.95, 56.80, 32.95, 24.99] ]    # Price per item

# [ordernumber, (article number, quantity, price per unit)]
data_set_2 = [ [34597, ("Learning Python, Mark Lutz", 4, 40.95)],
               [98762, ("Programming Python, Mark Lutz", 5, 56.80)],
               [77226, ("HeadFirst Python, Paul Barry", 3, 32.95)],
               [88112, ("Einfuhrung in Python3, Bernd Klein", 3, 24.99)] ]

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

def clean_data_a(data):
    cleaned_data = data
    
    for i, v in enumerate(cleaned_data[3]):
        if cleaned_data[2][i] * v < 100:
            cleaned_data[3][i] += 10

    return cleaned_data

def clean_data_b(data):
    cleaned_data = []

    for order in data:
        x = list(order[1])

        if x[1] * x[2] < 100:
            x[2] += 10

        cleaned_data.append((list([order[0], tuple(x)])))

    return cleaned_data

def function_a(data):
    """
    - [x] Write a Python program, which returns a list with 2-tuples.
          Each tuple consists of the order number and the product of
          the price per items and the quantity. The product should be
          increased by 10,- € if the value of the order is smaller than 100,00 €. 
    - [x] Write a Python program using lambda and map.
    """
    data = clean_data_a(data)

    return [ tuple([x for x in data[0]]), tuple([a * b for a, b in zip(data[2], data[3])]) ]

def function_b(data):
    """
    The same bookshop, but this time we work on a different list. The sublists of our lists look like this: 
    [ordernumber, (article number, quantity, price per unit), ... (article number, quantity, price per unit) ] 

    - [ ] Write a program which returns a list of two tuples with (order number, total amount of order).
    """
    data = clean_data_b(data)
    
    return list(map(lambda d: (d[0], d[1][1] * d[1][2]), data))

if __name__ == "__main__":
    display_assignment()

    print(function_a(data_set_1))
    print(function_b(data_set_2))
