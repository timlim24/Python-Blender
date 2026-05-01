import bpy
from helper_functions import *

os.system('cls' if os.name == 'nt' else 'clear')


def main():
    list_of_items = ['Cube', 'Camera']
    select_by_name(list_of_items)

def select_by_name(items):
    print(items)
    for objs in items:
        print(objs)
        bpy.data.objects[objs].select_set(True)

if __name__ == '__main__':
    main()
