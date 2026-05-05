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

    for i, obj in enumerate(so):
        if i % 2 == 0:
            obj.hide_viewport = True
        else:
            obj.hide_viewport = False

if __name__ == '__main__':
    main()
