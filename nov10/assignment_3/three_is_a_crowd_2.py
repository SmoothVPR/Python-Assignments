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
    - [x] Save your program from Three is a Crowd under a new name.
    - [x] Add an else statement to your if tests. If the else statement is run, have it print a message that the room is not very crowded.
    """
    def __init__(self, *args, **kwargs):
        self.people = []

    def add_people(self, names):
        self.people = names
    
    def is_crowded_test(self):
        return (len(self.people) > 3)

    def display_people(self):
        print("\nPeople in the room: ", self.people, "\n")

        if self.is_crowded_test():
            print("The room is crowded")
        else:
            print("The room is not crowded")

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
