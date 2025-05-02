from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.

This program fills boards of corners with checkerboard patterns.

Functions for scanning surroundings based on fulfilled conditions, and functions for even and odd horizontal row filling.

It has case considerations for different size boards and uses the 4 basic Karel movement functions implemented in various helper functions

Week 2 of Stanford CIP5 2025 course.
"""

def main():
    #check to see if karel is in a clear, top row, and if single column, or space to move
    #check for the corner, to then determine the action karel will start with, 
    #pre and post conditions for the even and odd paint functions, should all leave karel 
    #in the row above , first space, facing east. if no more rows above, Karel should
    #return to corner (0,0), facing east.
    #this indicates the starting condition for the program to run for however collumns
    # or rows we have.

    start_corner_and_middle_painting() #painting loops for Start and middle parts of the checkerboard 
    start_collumn_painting() #checks for collumn boards and 1x1 scenarios, paints and returns
    start_ceiling_row() #finishes the board painting process, then returns home
    corner_return() # for when karel finds themselves at the end of a board and 
                    # needs to return home  and face east.
    final_row_check()

#Painting Helper Functions, for Varios scenarios. combinations of odd and even line painters

def start_corner_and_middle_painting():
    #first scenario. Space above and in front of karel, but blocked on bottom.
    # Board has a floor, and or is middle space. Karel can freely place odd and even lines
    # in loop.
    #This function accounts for where Karel is starting, or following up from. and 
    #paints accordingly
    while front_is_clear() and left_is_clear() and right_is_blocked():
        # board with space above karel, and with more than one collumn, first line.
        # floor on bottom. all good to paint pairs of checker pattern.
        even_board_paint()
        odd_board_paint()

    while front_is_clear() and left_is_clear() and right_is_clear():
        #loop that will carry on for large sets of board area. 
        # pre condition: should come from an odd board painting
        even_board_paint()
        odd_board_paint()

def start_collumn_painting():
    #second scenario. karel detects the board to be a single collumn board,
    # where the front is blocked, left clear is clear. this is a vertical row method.
    # we will only face up, and start laying a checkered pattern, once done, will return home
    while front_is_blocked() and left_is_clear() and no_beepers_present():
        turn_left()
        while front_is_clear():
            safe_put_beeper()
            safe_move()
            safe_move()
        #Check for previous line, odd or even, put beeper accordingly, then return to base.
        collumn_check()
    while front_is_blocked() and left_is_blocked() and right_is_blocked() and no_beepers_present():
        put_beeper()

def start_ceiling_row():
    #third Scenario. final row, with space in column in front. this is for the final rows
    # including a check for previous row
    while front_is_clear() and left_is_blocked():
        #this runs the check previous line and paint function to account for fencepost problems.
        check_previous_line_and_paint()

    #final scenario.

def collumn_check():
    # Checks for to see if the line below is odd or even, and puts a beeper accordingly,
    # then return to the bottom corner of the collumn and face east
    turn_around()
    safe_move()
    if beepers_present():
        move_to_wall()
        turn_left()
    else:
        turn_around()
        move()
        turn_around()
        safe_put_beeper()
        move_to_wall()
        turn_left() 

def check_previous_line_and_paint():
    #This paints the last row in case the pair painting did not finish the job. considers odd
    #and even scenarios.
    turn_right()
    if front_is_clear():
        move()
        turn_around()
        if beepers_present():
            move()
            odd_board_paint()
        else:
            move()
            turn_right()
            even_board_paint()
    else:
        turn_left()
        even_board_paint()

def final_row_check():
    #check for the last row's status to see if even or odd. then return home
    if front_is_clear() and left_is_blocked() and no_beepers_present():
        #checks to see if in contact with ceiling, and if already a printed even row.
        even_board_paint()
    return_back_down()

# Core Painting Functions for Even and Odd Lines
def even_board_paint():
    #moves and places beeper with one space in between
    #Border Check, north side and east side should be clear before starting
    #pre condition, karel must be facing east
    while left_is_clear() and front_is_clear():
        safe_put_beeper()
        safe_move()
        safe_move()
    while left_is_blocked() and front_is_clear():
        safe_put_beeper()
        safe_move()
        safe_move()

    even_end_check()


def even_end_check():    
    # Scenario 1 finished line and needs festpost bug solving
    if left_is_clear() and front_is_blocked():
        turn_around()
        safe_move()
        if beepers_present():
            travel_back()

        else:
            turn_around()
            move()
            safe_put_beeper()
            turn_around()
            move_to_wall()
            step_back()

    #even line Post Fence Problem handling, and cheking for correct last beeper placement.
    #last_even_beeper_check_and_return()
    if left_is_blocked() and front_is_blocked():     

        safe_put_beeper()
    
def odd_board_paint():
    #first scenario, clear front, no beepers, coming in from even row, not single collumn
    if front_is_clear() and no_beepers_present():
        safe_move()
        while front_is_clear():
            safe_put_beeper()
            safe_move()
            safe_move()
        verify_last_space_odd()    
    else:
        #Verify last one
        verify_last_space_odd()
 
    #second Scenario
    if front_is_clear() and left_is_clear() and right_is_clear() and beepers_present():
        turn_left()
        safe_move()
        turn_right()

def verify_last_space_odd():
    #when hitting the end of an odd checkered line, this function checks for fencepost
    # bug, solves for it, or just returns home, like a carriage return.
    turn_around()
    safe_move()
    if beepers_present() and front_is_clear():
        # These commands confirm that the row is complete, and just returns karel and sends 
        #to the next row available to follow the main logic again
        move_to_wall()
        step_back()

    if no_beepers_present() and front_is_clear() and left_is_clear() and right_is_clear():
        # once returned to the second to last space, Karel verifies lack of beeper 
        # presence, these commands ensure the last spot has the fencepost bug is fixed.
        turn_around()
        safe_move()
        safe_put_beeper()
        turn_around()
        travel_back()
   
    if no_beepers_present() and front_is_clear() and left_is_clear() and right_is_blocked():

        turn_around()
        safe_move()
        safe_put_beeper()
        turn_around()
        move_to_wall()
        turn_left()
        move_to_wall()
        turn_left()

def return_back_down():
    #moves Karel from starting position of row, all the way down to bottom collumn and 
    #facing east
    while not_facing_south():
        turn_left()
    move_to_wall()
    turn_left()

def travel_back():
    #while facing east, karel will turn around, and walk to beginning of hallway,
    # to then try to move to the next row.
    move_to_wall()
    if right_is_clear():
        step_back()

def corner_return():
    # for when karel finds herself at the end of a board and needs to return home 
    # and face east.
    while front_is_blocked() and left_is_blocked():
        turn_around()
        move_to_wall()
        turn_left()
        move_to_wall()
        turn_left()    

# Basic movement Helper functions
def move_to_wall():
    while front_is_clear():
        move()

def turn_around():
    turn_left()
    turn_left()

def turn_right():
    for i in range(3):
        turn_left()

def safe_move():
    if front_is_clear():
        move()

def safe_put_beeper():
    if no_beepers_present():
        put_beeper()

def step_back():
    turn_right()
    safe_move()
    turn_right()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
