import bpy
import os
from helper_functions import *


def main():
    clear_console()
    # select(types = 'ALL')

    base = 8
    size = 3
    tall = 5
    reset = x = y = z = 0.5 * size

    for height in range(tall):
        for depth in range(base):
            for width in range(base):
                add_mesh('Cube', size = size, location = (x,y,z))
                x += size
            y += size
            x = reset
        y = reset
        z += size

    # so = bpy.context.selected_objects
    # sorted_so = sorted(so, key = lambda obj: obj.name)

    # for i, obj in enumerate(sorted_so):
    #     print(obj.name)
    #     sorted_so[i].location.z = i * 2

if __name__ == '__main__':
    main()
