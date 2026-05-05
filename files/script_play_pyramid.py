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
            x = reset * (height + 1)
        x = reset * (height + 2)
        y = reset * (height + 2)
        z += size
        base -= 1

if __name__ == '__main__':
    main()
