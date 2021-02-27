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
    return print('+-------   -------+\n'
                 '|                 |\n'
                 '|                 |\n'
                 '|        O         \n'
                 '|                 |\n'
                 '|                 |\n'
                 '+-------   -------+\n')

def room_UDL():
    clear()
    return print('+-------   -------+\n'
                 '|                 |\n'
                 '|                 |\n'
                 '         O        |\n'
                 '|                 |\n'
                 '|                 |\n'
                 '+-------   -------+\n')

def room_URL():
    clear()
    return print('+-------   -------+\n'
                 '|                 |\n'
                 '|                 |\n'
                 '         O         \n'
                 '|                 |\n'
                 '|                 |\n'
                 '+-----------------+\n')

def room_RDL():
    clear()
    return print('+-----------------+\n'
                 '|                 |\n'
                 '|                 |\n'
                 '         O         \n'
                 '|                 |\n'
                 '|                 |\n'
                 '+-------   -------+\n')

# ------------------------------------------

# FOUR DOOR ROOM: --------------------------

def room_URDL():
    clear()
    return print('+-------   -------+\n'
                 '|                 |\n'
                 '|                 |\n'
                 '         O         \n'
                 '|                 |\n'
                 '|                 |\n'
                 '+-------   -------+\n')
# ------------------------------------------

one_door_rooms = [1, 2, 3, 4]
two_door_rooms = [5, 6, 7, 8, 9, 10]
three_door_rooms = [room_URD, room_UDL, room_URL, room_RDL]
four_door_rooms = [room_URDL]

grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

pos_x_y = [4, 6]
room_count = 1

room_desc_list = [ ''

]

room_desc_dict = {
    1: 'This is the beginning room. Nothing special here.',
}

room_doors_dict = {
    1: room_URDL,

}

# Game Start ======================================================================================
new_prompt('You wake up to the sound of echoing bats. (Press Enter)')
new_prompt("The hard surface you're laying on is slightly wet.")
new_prompt('You open your eyes and look around. There is a single torch lighting up a small room.')
new_prompt('You find a compass sitting on your chest.')
new_prompt('The square room has four doors, one on each wall. You decide to explore.')
# =================================================================================================

room_doors_dict[room_count]()

user_choice = input('Enter a direction -- North:[w], West:[a], South:[s], East:[d]. Enter [q] to quit\n')


while user_choice != 'q':
    if user_choice == 'w':
        if len(grid) - 1 >= pos_x_y[1] > 0:
            pos_x_y[1] -= 1
        else:
            print("You've come across a wall.")
            sleep(.5)
            user_choice = input('Enter a direction or enter [q] to quit\n')
            continue
    elif user_choice == 'a':
        if len(grid) - 1 >= pos_x_y[0] > 0:
            pos_x_y[0] -= 1
        else:
            print("You've come across a wall.")
            sleep(.5)
            user_choice = input('Enter a direction or enter [q] to quit\n')
            continue
    elif user_choice == 's':
        if len(grid) - 1 > pos_x_y[1] >= 0:
            pos_x_y[1] += 1
        else:
            print("You've come across a wall.")
            sleep(.5)
            user_choice = input('Enter a direction or enter [q] to quit\n')
            continue    
    elif user_choice == 'd':
        if len(grid) - 1 > pos_x_y[0] >= 0:
            pos_x_y[0] += 1
        else:
            print("You've come across a wall.")
            sleep(.5)
            user_choice = input('Enter a direction or enter [q] to quit\n')
            continue
    elif user_choice == 'g':
        for i in grid:
            print(i)
        input('Press Enter to return.')
    else:
        print('Invalid selection.')
        sleep(.5)
        user_choice = new_prompt('Enter a direction, enter [g] to view grid or enter [q] to quit')
        continue

# FIXME: Each newly visted room should be random. Overwrite grid coordinate if value == 0 using pos_x_y. 
# FIXME: Replace 0 value in grid with room_count value and increment room_count value by 1. Associate room_count
# FIXME: value with index of room_doors_dict to track the type of visted room.
    if grid[pos_x_y[1]][pos_x_y[0]] == 0:
        room_count += 1
        grid[pos_x_y[1]][pos_x_y[0]] = room_count

        # vvv Makes the beginning rooms have more door options
        if room_count <= 5:
            room_doors_dict[room_count] = four_door_rooms[0] #I Think this works now, but I'm testing other stuff
            room_doors_dict[room_count]()
            pass
        elif room_count <= 10:
            room_doors_dict[room_count] = random.choice(four_door_rooms)
            pass
        elif room_count <= 20:
            pass
        else:
            pass
    else:
        print('already visted this room.') #FIXME: Replace this with a function call based on the room count designated for this room
        sleep(.5)
       

# if:
#   random room code
#   assign new key:value in room_doors_dict with result of key: room_count, value: random door function
# else:
#   use grid coordinate value to search room_doors_dict for value: random door function
    
    user_choice = input('Enter a direction or enter [q] to quit\n')

print('Thanks for playing!')




