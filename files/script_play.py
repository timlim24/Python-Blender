import bpy
import os
from helper_functions import *

os.system('cls' if os.name == 'nt' else 'clear')


def main():
    select()

def select(*object_names, **kwargs):
    '''
    This function is designed to select multiple
    objects by their name and types.

    select() will deselect all objects
    select(types='ALL') will select all objects
    select(types=['MESH', 'EMPTY']) will sellect all of that type.
    select('name') will select objects by their name.
    '''
    types = kwargs.get('types')

    # Check if objects exist
    number_of_objects = len(object_names)
    if number_of_objects == 0:
        print('No Objects')

    else:
        match types:
            case None | []:
                for obj in all_objects():
                    obj.select_set(False)
            case 'ALL':
                for obj in all_objects():
                    obj.select_set(True)
            case _:
                for obj in all_objects():
                    if obj.type in types:
                        obj.select_set(True)
                    else:
                        obj.select_set(False)

        # Select objects by name
        if object_names is not None:
            for objs in object_names:
                all_objects()[objs].select_set(True)

def all_objects():
    return bpy.data.objects

if __name__ == '__main__':
    main()
