import bpy
import os

from math import sin, cos, radians
from helper_functions import *


def main():
    clear_console()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Object Parameters
    object_size = 1
    object_type = 'Monkey'
    number_of_objects = 12
    x = y = z = 0

    # Circle Parameters
    radius = 5
    angle_between_objects = 360 / number_of_objects

    for obj in range(number_of_objects):
        angle = radians(obj * angle_between_objects)

        x = cos(angle) * radius
        y = sin(angle) * radius

        add_mesh(object_type, size = object_size, location = (x,y,z))

        rot_angle = radians(-90 - obj * angle_between_objects)

        bpy.ops.transform.rotate(value=rot_angle, orient_axis='Z')

if __name__ == '__main__':
    main()
