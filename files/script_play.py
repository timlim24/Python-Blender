import bpy
import os

from math import sin, cos, radians, exp
from helper_functions import *


def main():
    clear_console()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Object Parameters
    object_size = 1
    object_type = 'Cube'
    number_of_objects = 800
    x = y = z = 0

    # Spiral Parameters
    spiral_radius = 1
    angle_between_objects = 360 / number_of_objects
    spiral_height = 15
    rotation_factor = 8

    for obj in range(number_of_objects):
        placement_angle = rotation_factor * obj * angle_between_objects
        angle = radians(placement_angle)

        vortex_calculation = exp(obj*.005) * spiral_radius

        x = cos(angle) * vortex_calculation
        y = sin(angle) * vortex_calculation

        add_mesh(object_type, size = object_size, location = (x,y,z))

        rot_angle = radians(-90 - placement_angle)

        bpy.ops.transform.rotate(value=rot_angle, orient_axis='Z')

        z += spiral_height / number_of_objects

if __name__ == '__main__':
    main()
