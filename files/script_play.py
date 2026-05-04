import bpy
import os
from helper_functions import *

os.system('cls' if os.name == 'nt' else 'clear')


def main():
    select()

def select(*object_names, type=None):
    '''
    This function is designed to select multiple
    objects by their name and type.

    select(type='ALL') will select all objects
    '''
    # Check if objects exist
    number_of_objects = len(object_names)
    if number_of_objects == 0:
        print('No Objects')
    else:
        if type == 'ALL':
            for obj in all_objects():
                obj.select_set(True)


    # print(object_names)
    # for objs in object_names:
    #     print(objs)
    #     all_objects()[objs].select_set(True)

def all_objects():
    return bpy.data.objects

if __name__ == '__main__':
    main()
