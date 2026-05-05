import bpy
import os

from math import sin, cos, radians
from helper_functions import *


def main():
    clear_console()
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete(use_global=False)

    # Object Parameters
    object_size = 1.8
    object_type = 'Cube'
    number_of_objects = 24
    x = y = z = 0

    # Circle Parameters
    radius = 5
    angle_between_objects = 360 / number_of_objects

    number_of_layers = 10
    distance_between_layers = 2

    for layer in range(number_of_layers):

        for obj in range(number_of_objects):
            placement_angle = obj * angle_between_objects
            angle = radians(placement_angle)

            x = cos(angle) * radius
            y = sin(angle) * radius

            add_mesh(object_type, size = object_size, location = (x,y,z))

            rot_angle = radians(-90 - placement_angle)

            bpy.ops.transform.rotate(value=rot_angle, orient_axis='Z')

            z += distance_between_layers / number_of_objects

#        z += distance_between_layers

if __name__ == '__main__':
    main()
