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


#PERSISTENCE FOR JSON
def load_json():
    path = 'ntz.json'
    with open(path, 'r') as f:
        lists_data = json.load(f)
    return lists_data

def dump_json(lists_data):
    path = 'ntz.json'
    with open(path, 'w') as f:
        json.dump(path, f)


def remember (note):
    lists_data = load_json()

    #add remember logic
    print(note)

def forget():
    lists_data = load_json()
    #add forget logic
    dump_json(lists_data)
    pass

def create():
    to_do_list = load_json()
    if new_list not in to_do_list:
        new_dict = {new_list: []}
        #add new dict to to do lists dict
        dump_json(to_do_list)
    else:
        print('To Do List already exists. Please edit or create a new list.')


def edit():
    lists_data = load_json()
    #select list to edit
    #add to list
    #remove from list
    dump_json(lists_data)
    pass

def clear():
    lists_data = load_json()
    #select list to clear
    #confirm clear
    #clear list
    dump_json(lists_data)
    pass

def ntz_help():
    print('')
    print('To make a new list use: -c "new list name"\n')
    print('To remember a list or items use: -r "list name"\n')
    print('To forget a list use: -f "list name"\n')
    print('To edit a list use: -e "list name"\n')
    print('To clear a list use: clear "list name"\n')


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
