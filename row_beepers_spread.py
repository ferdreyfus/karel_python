from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    move()
    find_beepers()
    
def find_beepers():
    # move away from west wall, pick beeper, check to see if space is empty, then end,
    # if space not empty, spread beeper to front.
    # First Beeper Check, picks beeper, if last one to be picked, then return home.
    # if there's still beepers there, then spread the one just picked up to the end.
    while beepers_present():
        pick_beeper()
        if beepers_present():
            move()
            spread_beeper()
            move()
        else:
            put_beeper()
            rehome()

def spread_beeper():
    # after picking up a beeper, this moves karel to front of line to drop beeper and
    # return to the start of the puzzle.
    while beepers_present():
        move()
    put_beeper()
    rehome()

def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()
    
def rehome():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
