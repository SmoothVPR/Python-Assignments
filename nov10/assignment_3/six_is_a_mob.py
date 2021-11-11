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
    Save your program from Three is a Crowd - Part 2 under a new name.
    Add some names to your list, so that there are at least six people in the list.
    Modify your tests so that:
    - [ ] If there are more than 5 people, a message is printed about there being a mob in the room.
    - [ ] If there are 3-5 people, a message is printed about the room being crowded.
    - [ ] If there are 1 or 2 people, a message is printed about the room not being crowded.
    - [ ] If there are no people in the room, a message is printed about the room being empty.

    """
    def __init__(self, *args, **kwargs):
        self.people = []

    def add_people(self, names):
        self.people = names
    
    def display_people(self):
        print("\nPeople in the room: ", self.people, "\n")
        size = len(self.people)
        if size < 1:
            print("Where is everybody...?")
        elif size < 2:
            print("The room isn't too crowded...")
        elif size < 6:
            print("The room is too crowded!")
        else:
            print("Who let the mob in here!?")

    def is_crowded_test(self):
        return (len(self.people) > 3)

    def run(self):
        while len(self.people) > 0:
            self.display_people()

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

    names = [ "Adam", "Cain", "Abel", "John", "James", "Jack", "Dan", "David" ]
    
    game = Game()
    assert game_is_crowded_test(game) == False

    game.add_people(names)
    assert game_is_crowded_test(game) == True

    game.run()
    assert game_is_crowded_test(game) == False

    game.display_people()
