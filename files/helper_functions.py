import bpy
import os

os.system('cls' if os.name == 'nt' else 'clear')

def select_objects():
    bpy.ops.object.select_all(action='SELECT')

select_objects()
