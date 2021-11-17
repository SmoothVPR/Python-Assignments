#!/usr/bin/env python3

"""
Author:   Malik R Booker
Created:  November 10, 2021
Modified: November 10, 2021
"""

from random import randint

DAY = 2
EXERCISE = 6

class Game(object):
    """
    - [x] Make a list of names that includes at least four people.
          Write an if test that prints a message about the room being
          crowded, if there are more than three people in your list.
    - [x] Modify your list so that there are only two people in it. Use one 
          of the methods for removing people from the list, don't just redefine
          the list.
    - [x] Run your if test again. There should be no output this time, because there are less than three people in the list.

    Bonus:
    - [x] Store your if test in a function called something like crowd_test.
    """
    def __init__(self, *args, **kwargs):
        self.people = []

    def add_people(self, names):
        self.people = names
    
    def display_people(self):
        print("\nPeople in the room: ", self.people, "\n")

    def is_crowded_test(self):
        return (len(self.people) > 3)

    def run(self):
        while self.is_crowded_test():
            random_idx = randint(0, len(self.people)-1)

            print("Room is crowded! Removing ", self.people[random_idx], "...", sep="")
            self.people.pop(random_idx)

# Kinda unnecessay but I'm trying to get them bonus points
def game_is_crowded_test(game):
    return game.is_crowded_test()

def display_assignment():
    print( "###############")
    print(f"# Day: {DAY}      #")
    print(f"# Exercise: {EXERCISE} #")
    print( "###############")
    print("")

if __name__ == "__main__":
    display_assignment()

    names = [ "Adam", "Cain", "Abel", "John", "James" ]
    
    game = Game()
    assert game_is_crowded_test(game) == False

    game.add_people(names)
    game.display_people()
    assert game_is_crowded_test(game) == True

    game.run()
    game.display_people()
    assert game_is_crowded_test(game) == False

