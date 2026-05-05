import bpy
import os
from helper_functions import *


def main():
    clear_console()
    # select(types = 'ALL')
    x = 0
    y = 0
    z = 5
    so = bpy.context.selected_objects

    so[0].location = (x,y,z)
    so[1].location = (x,y,z)

if __name__ == '__main__':
    main()
