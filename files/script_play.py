import bpy
import os
from helper_functions import *


def main():
    clear_console()
    # select(types = 'ALL')

    size = 1
    base = 6
    x = y = z = 0.5 * size

    for width in range(base):
        add_mesh('Cube', size = size, location = (x,y,z))
        x += size

    # so = bpy.context.selected_objects
    # sorted_so = sorted(so, key = lambda obj: obj.name)

    # for i, obj in enumerate(sorted_so):
    #     print(obj.name)
    #     sorted_so[i].location.z = i * 2

if __name__ == '__main__':
    main()
