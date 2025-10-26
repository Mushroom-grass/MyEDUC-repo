import bpy

print("=======================")
print("====== mesh and its materials ======")
for obj in bpy.data.objects:
    if obj.type == 'MESH':
#        print(obj.name + ": " + str(obj.data.materials))
        for slot in obj.material_slots:
            if slot.material != None:
                print(obj.name + ": " + slot.material.name)

        
    
print("===== Only Meshes =====")    
for mesh in bpy.data.meshes:
    if mesh.materials != None:
        print(mesh.name + ": " + str(mesh.materials))
    
print("===== Only Materials =====")
for mat in bpy.data.materials:
    print(mat.name)