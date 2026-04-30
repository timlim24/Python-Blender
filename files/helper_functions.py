import bpy
import os

os.system('cls' if os.name == 'nt' else 'clear')

def main():
    deselect_all_objects()
    select_all_object_type('LIGHT')

def select_all_object_type(obj_type='MESH'):
    '''
    '''
    objects = bpy.data.objects
    for obj in objects:
        if obj.type == obj_type:
            obj.select_set(True)

def select_all_objects():
    bpy.ops.object.select_all(action='SELECT')

def deselect_all_objects():
    bpy.ops.object.select_all(action='DESELECT')


if __name__ == '__main__':
    main()
