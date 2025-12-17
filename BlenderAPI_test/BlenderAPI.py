import bpy
import os

blend_path = bpy.data.filepath          # 当前 .blend 的完整路径
blend_dir  = os.path.dirname(blend_path)  # 所在文件夹
print("=======================")
print(blend_dir)



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
#    print(mat.name)
    
    if not mat.use_nodes:
        mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    image_nodes = [n for n in nodes if n.type == 'TEX_IMAGE']
    if image_nodes:
        for n in image_nodes:
#            if n.image:
                print("Material:", mat.name, "Image:", n.image.name, "Path:", n.image.filepath)
    else: 
        print("Material:", mat.name, "Image: None")


    