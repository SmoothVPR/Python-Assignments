#!/usr/bin/env python3

"""
Author:    Malik R Booker
Created:   November 16, 2021
Completed: November 16, 2021
Modified:  November 16, 2021
Brief:
    - [x] Import numpy
    - [x] Create an array of 10 zeros
    - [x] Create an array of 10 ones
    - [x] Create an array of 10 fives
    - [x] Create an array of integers from 10 to 50
    - [x] Create an array of even integers from 10 to 50
    - [x] Create a 3x3 matrix with values ranging from 0 to 8
    - [x] Create a 3x3 identity matrix
    - [x] Use numpy to randomly generate a number between 0 and 1
"""

import numpy as np

def excercise_a() -> np.ndarray:
    return np.zeros(10)

def excercise_b() -> np.ndarray:
    return np.array([1. for _ in range(10)])

def excercise_c() -> np.ndarray:
    return np.array([5. for _ in range(10)])

def excercise_d() -> np.ndarray:
    return np.array([x for x in range(10, 51)])

def excercise_e() -> np.ndarray:
    return np.array([x for x in range(10, 51)if x % 2 == 0])

def excercise_f() -> np.matrix:
    return np.matrix([[x for x in range(0, 3)],
                      [x for x in range(3, 6)],
                      [x for x in range(6, 9)]] )

def excercise_g() -> np.ndarray:
    return np.eye(3)

def excercise_h() -> int:
    return np.random.randint(0, 10)

DAY = 6

if __name__ == "__main__":
    print(excercise_a())
    print(excercise_b())
    print(excercise_c())
    print(excercise_d())
    print(excercise_e())
    print(excercise_f())
    print(excercise_g())
    print(excercise_h())
