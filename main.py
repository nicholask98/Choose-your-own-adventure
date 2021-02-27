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

def room_UDL():
    clear()
    print(' -------   ------- ')
    print('|                 |')
    print('|                 |')
    print('         O        |')
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

room_desc_list = ['This is just an empty room',
                  'This room smells like oil,',
                  'You walk in a regret your life beacuse it\'s led you to this',
                  'This room nasty.']


# POSITIONING At Game Start-----------------
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

room_doors_dict = {
    1: room_URDL,
}

room_desc_dict = {
    1: "Starting Room"
}
# ------------------------------------------

# Game Start ======================================================================================
new_prompt('You wake up to the sound of echoing bats. (Press Enter)')
new_prompt("The hard surface you're laying on is slightly wet.")
new_prompt('You open your eyes and look around. There is a single torch lighting up a small room.')
new_prompt('You find a compass sitting on your chest.')
new_prompt('The square room has four doors, one on each wall. You decide to explore.')
# =================================================================================================

room_doors_dict[room_count]()
print(room_desc_dict[room_count])
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
    else:
        print('Invalid selection.')
        sleep(.5)
        user_choice = new_prompt('Enter a direction or enter [q] to quit')
        continue

    print('valid entry')
    print('coordinates:{},{}'.format(pos_x_y[0], pos_x_y[1]))
    sleep(.5)

# FIXME: Each newly visted room should be random. Overwrite grid coordinate if value == 0 using pos_x_y. 
# FIXME: Replace 0 value in grid with room_count value and increment room_count value by 1. Associate room_count
# FIXME: value with index of room_doors_dict to track the type of visted room.

    if grid[pos_x_y[1]][pos_x_y[0]] == 0:
        room_count += 1
        print('room count: {}'.format(room_count))
        grid[pos_x_y[1]][pos_x_y[0]] = room_count
        for i in grid:
            print(i)
        sleep(.5)
        # vvv Makes the beginning rooms have more door options
        if room_count <= 5:
            room_doors_dict[room_count] = random.choice(four_door_rooms)
            room_desc_dict[room_count] = random.choice(room_desc_list)
            print(room_doors_dict[room_count]())
            print(room_desc_dict[room_count])
            sleep(5)
            pass
        elif room_count <= 10:
            pass
        elif room_count <= 20:
            pass
        else:
            pass
    else:
        print('already visted this room.')
        sleep(.5)
    
    user_choice = new_prompt('Enter a direction or enter [q] to quit')

print('Thanks for playing!')




