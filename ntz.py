# What's it look like?
# ntz has four commands.
# [r]emember
# [-c] creates or appends to a category
# [f]orget a note
# [e]dit a note
# clear

import sys
from sys import argv
import json


#ADD PERSISTENCE LOGIC
# json load
#json dump

def remember (note):
    #add json persist
    #add remember logic
    print(note)

def forget():
    #add json persist
    #add forget logic
    pass

def create():
    to_do_list = #json loads function
    if new_list not in to_do_list:
        new_dict = {new_list: []}
        #json dump(to_do_list)
    else:
        print('To Do List already exists. Please edit or create a new list.')


def edit():
    pass

def clear():
    pass

def help():
    pass

def main():
    arg = argv[1]
    if arg == 'r':
        remember(argv[2])
    elif arg == 'f':
        forget()
    elif arg == 'c':
        create(argv[2])
    elif arg == 'e':
        edit()
    elif arg == 'clear':
        clear()
    elif arg == 'help':
        ntz_help()
    else:
        print ('Invalid input')
        ntz_help()



main()
