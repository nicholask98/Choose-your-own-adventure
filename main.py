# import only system from os 
from os import system, name
  
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
    input(a + '\n')

def starting_room():
    pass











new_prompt('You wake up to the sounds of segulls chirping. (Press Enter)')
new_prompt('The ocean waves crash nearby.')
new_prompt('You open your eyes and look around')
new_prompt('')