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
    min_scale = 0.5
    max_scale = 2

    # Volume Parameters
    vol_x = 20
    vol_y = 20
    vol_z = 5

    objects = []

    for obj in range(number_of_objects):

        scale = random.uniform(min_scale, max_scale)

        x = random.uniform(-vol_x / 2, vol_x / 2)
        y = random.uniform(-vol_y / 2, vol_y / 2)
        z = random.uniform(-vol_z / 2, vol_z / 2)

        rot_x = random.uniform(0, 360)
        rot_y = random.uniform(0, 360)
        rot_z = random.uniform(0, 360)

        #Check Intersection Here:
        if not intersecting(x, y, z, scale, object_size, objects):

            add_mesh(object_type, size = object_size)
            object = bpy.context.object

            object.location = (x, y, z)
            object.scale = (scale, scale, scale)
            object.rotation_euler = (rot_x, rot_y, rot_z)

            objects.append((x, y, z, scale))


def intersecting(x, y, z, scale, object_size, objects):
    for object in objects:
        x_dist = (x - object[0])**2
        y_dist = (y - object[1])**2
        z_dist = (z - object[2])**2

        distance = math.sqrt(x_dist + y_dist + z_dist)

        added_object = math.sqrt(3 * (object_size * scale * 0.5) ** 2)
        existing_object = math.sqrt(3 * (object_size * object[3] * 0.5) ** 2)

        if distance < added_object + existing_object:
            return True
    return False

if __name__ == '__main__':
    main()
