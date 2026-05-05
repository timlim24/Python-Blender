import bpy
import os
import random
import math

from helper_functions import *


def main():
    clear_console()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Object Parameters
    object_type = 'Cube'
    object_size = 1
    number_of_objects = 100
    x = y = z = 0

    # Volume Parameters
    vol_x = 20
    vol_y = 5
    vol_z = 5

    for obj in range(number_of_objects):

        x = random.uniform(-vol_x/2, vol_x/2)
        y = random.uniform(-vol_y/2, vol_y/2)
        z = random.uniform(-vol_z/2, vol_z/2)

        add_mesh(object_type, size = object_size)
        object = bpy.context.object
        object.location = (x,y,z)


if __name__ == '__main__':
    main()
