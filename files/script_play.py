import bpy
import os
from helper_functions import *

os.system('cls' if os.name == 'nt' else 'clear')


def main():
    list_of_items = ['Cube', 'Camera']
    select_by_name(list_of_items)

def select_by_name(items):
    print(items)
    for objs in items:
        print(objs)
        all_objects()[objs].select_set(True)

def all_objects():
    return bpy.data.objects

if __name__ == '__main__':
    main()
