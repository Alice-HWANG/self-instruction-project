"""
File: Steeplechase.py
Name: ALICE HWANG
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()
            turn_left()
    move()
    jump()


def  jump():
    """
    pre-condition:Karel is on the left,facing East.
    post-condition:Karel is on the right.
    """
    up()
    cross()
    down()

def up():
    """
    pre-condition:Karel is on the left,facing East.
    post-condition:Karel is on the upper left,facing North.
    """
    # while not front_is_clear():
    #     turn_left()
    #     move()
    #     turn_right()
    turn_left()
    # Karel is facing North,walls on the right.
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()

def cross():
    """
    pre-condition:Karel is on the upper left,facing North.
    post-condition:Karel is on the right,facing South.
    """
    turn_right()
    move()
    turn_right()

def down():
    """
    pre-condition:Karel is on the upper right,facing South.
    post-condition:Karel is
    """
    while front_is_clear():
        move()




# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
