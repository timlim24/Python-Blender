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

    def object_name(obj):
        return obj.name

    sorted_so = sorted(so, key = object_name)

    for i, obj in enumerate(sorted_so):
        print(obj.name)
        sorted_so[i].location.z = i * 2

#    for i, obj in enumerate(objs):
#        objs[i].location.z = i * 2
#        obj.hide_viewport = False
#        if i % 2 == 0:
#            obj.hide_viewport = True
#        else:
#            obj.hide_viewport = False

if __name__ == '__main__':
    main()
