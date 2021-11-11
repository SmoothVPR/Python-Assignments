#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 10, 2021
Modified: November 10, 2021
"""

DAY = 2
EXERCISE = 3

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

def exercise_3_a(string):
    """
    Write a string that returns just the letter ‘r’ from ‘Hello World’
    """
    print("exercise_3_a")
    print(string[string.find("r")])
    print("")

def exercise_3_b(string_1, string_2):
    """
    String slicing to grab the word ‘ink’ from the word  ‘thinker’
    S=’hello’,what is the output of h[1]
    """
    print("exercise_3_b")
    print(string_1[2:5])
    print(string_2[1])
    print("")

def exercise_3_c(string):
    """
    S=’Sammy’ what is the output of s[2:]”
    """
    print("exercise_3_c")
    print(string[2:])
    print("")

def exercise_3_d(string):
    """
    With a single set function can you turn the word ‘Mississippi’ to distinct character word.
    """

    print("".join(sorted(set(string))))
    print("")

def exercise_3_e():
    """
    Your goal in this programming exercise is to determine, whether the phrase
    represents a palindrome or not. Input data contains number of phrases in the  
    first line.
    Next lines contain one phrase each.
    Answer should have a single letter (space separated) for each phrase: Y if it
    is a palindrome and N if not.
    """

    result = ""

    ignored_chars = " ~!@#$%^&*()-=_+[]{}<>?,./;':\"\\|"

    n = int(input("input data:"))
    for _ in range(n):
        isPalindrome = True
        string = input()

        # remove unwanted characters
        string = "".join(list(filter(lambda c: c not in ignored_chars, string)))

        i, j = 0, len(string)-1
        while i < j:
            if string[i].upper() != string[j].upper():
                isPalindrome = False
                break;
            i += 1
            j -= 1


        if isPalindrome == True:
            result += "Y "
        else:
            result += "N "

    print(result)

if __name__ == "__main__":
    display_assignment()
    
    exercise_3_a("Hello World")
    exercise_3_b("thinker", "hello")
    exercise_3_c("Sammy")
    exercise_3_d("Mississippi")
    exercise_3_e()
