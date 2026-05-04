import bpy
import os
from helper_functions import *

os.system('cls' if os.name == 'nt' else 'clear')


def main():
    select_by_name('Cube', 'Camera')

def select_by_name(*object_names):
    print(object_names)
    for objs in object_names:
        print(objs)
        all_objects()[objs].select_set(True)

def all_objects():
    return bpy.data.objects

if __name__ == '__main__':
    main()
