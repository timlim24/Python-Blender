import bpy
import os
from helper_functions import *


def main():
    clear_console()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Object Parameters
    object_size = 1
    object_type = 'Cube'
    number_of_objects = 12
    x = y = z = 0

    # Circle Parameters
    radius = 5
    angle_between_objects = 360 / number_of_objects

    angle = radians(30)

    x = cos(angle) * radius
    y = sin(angle) * radius

    add_mesh(object_type, size = object_size, location = (x,y,z))

if __name__ == '__main__':
    main()
