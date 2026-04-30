import bpy
import os
import math

os.system('cls' if os.name == 'nt' else 'clear')

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

cube_loc = (0,0,1)
cube_rot = (0, 0, math.radians(30))
cylinder_loc = (0,0,3)
cylinder_rot = (math.radians(30), math.radians(90), 0)
monkey_loc = (0, 0, 4.44)
monkey_rot = (math.radians(-21), 0, math.radians(150))


bpy.ops.mesh.primitive_cube_add(location=cube_loc, rotation=cube_rot)
bpy.ops.mesh.primitive_cylinder_add(location=cylinder_loc, rotation=cylinder_rot)
bpy.ops.mesh.primitive_monkey_add(location=monkey_loc, rotation=monkey_rot)

cube = bpy.data.objects['Cube']
cylinder = bpy.data.objects['Cylinder']
suzanne = bpy.data.objects['Suzanne']

cube.select_set(True)
cylinder.select_set(True)
suzanne.select_set(True)
