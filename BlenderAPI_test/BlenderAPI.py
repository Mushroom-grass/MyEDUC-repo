import bpy

scene = bpy.data.scenes
for obj in bpy.data.objects:
    if obj.type == 'MESH':
        print(obj.name)