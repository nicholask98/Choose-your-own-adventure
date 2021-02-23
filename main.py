import random
# import only system from os 
from os import system, name

from time import sleep 

# define our clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

def new_prompt(a):
    clear()
    b = input(a + '\n')
    return b

# ONE DOOR ROOMS: --------------------------

def room_U():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('|        O        |')
    print('|                 |')
    print('|                 |')
    print(' ----------------- ')

def room_R():
    clear()
    print(' ----------------- ')
    print('|                 |')
    print('|                 |')
    print('|        O         ')
    print('|                 |')
    print('|                 |')
    print(' ----------------- ')

def room_D():
    clear()
    print(' ----------------- ')
    print('|                 |')
    print('|                 |')
    print('|        O        |')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

def room_L():
    clear()
    print(' ----------------- ')
    print('|                 |')
    print('|                 |')
    print('         O        |')
    print('|                 |')
    print('|                 |')
    print(' ----------------- ')

# ------------------------------------------

# TWO DOOR ROOMS: --------------------------

def room_UR():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('|        O         ')
    print('|                 |')
    print('|                 |')
    print(' ----------------- ')

def room_UD():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('|        O        |')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

def room_UL():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('         O        |')
    print('|                 |')
    print('|                 |')
    print(' ----------------- ')

def room_RD():
    clear()
    print(' ----------------- ')
    print('|                 |')
    print('|                 |')
    print('|        O         ')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

def room_RL():
    clear()
    print(' ----------------- ')
    print('|                 |')
    print('|                 |')
    print('         O         ')
    print('|                 |')
    print('|                 |')
    print(' ----------------- ')

def room_DL():
    clear()
    print(' ----------------- ')
    print('|                 |')
    print('|                 |')
    print('         O        |')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

# ------------------------------------------

# THREE DOOR ROOMS: ------------------------

def room_URD():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('|        O         ')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

def room_URL():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('         O         ')
    print('|                 |')
    print('|                 |')
    print(' ----------------- ')

def room_RDL():
    clear()
    print(' ----------------- ')
    print('|                 |')
    print('|                 |')
    print('         O         ')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

def room_URD():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('         O        |')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

# ------------------------------------------

# FOUR DOOR ROOM: --------------------------

def room_URDL():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('         O         ')
    print('|                 |')
    print('|                 |')
    print(' -------   ------- ')

# ------------------------------------------

one_door_rooms = [1, 2, 3, 4]
two_door_rooms = []
room_options = []

grid = [[0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0]]

pos_x_y = [2, 4]
room_count = 1
room_list = []

# FIXME: Each newly visted room should be random. Overwrite grid coordinate if value == 0 using pos_x_y. 
# FIXME: Replace 0 value with room_count value and increase room_count value. Associate room_count
# FIXME: value with index of room_list to track the type of visted room.

new_prompt('You wake up to the sounds of segulls chirping. (Press Enter)')
new_prompt('The ocean waves crash nearby.')
new_prompt('You open your eyes and look around')
user_choice = new_prompt('Enter a direction -- up:[w], left:[a], down:[s], right:[d]. Enter [q] to quit')

while user_choice != 'q':
    if user_choice == 'w':
        if 4 >= pos_x_y[1] > 0:
            pos_x_y[1] -= 1
        else:
            print("You've come across a wall.")
    elif user_choice == 'a':
        if 4 >= pos_x_y[0] > 0:
            pos_x_y[0] -= 1
        else:
            print("You've come across a wall.")
    elif user_choice == 's':
        if 4 > pos_x_y[1] >= 0:
            pos_x_y[1] += 1
        else:
            print("You've come across a wall.")        
    elif user_choice == 'd':
        if 4 > pos_x_y[0] >= 0:
            pos_x_y[0] += 1
        else:
            print("You've come across a wall.")
        
    else:
        new_prompt('Invalid selection.')
    print('coordinates:{},{}'.format(pos_x_y[0], pos_x_y[1]))
    sleep(.5)
    user_choice = new_prompt('Enter a direction or enter [q] to quit')

print('Thanks for playing!')




