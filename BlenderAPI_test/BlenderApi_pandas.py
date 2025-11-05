import bpy, csv
import pandas as pd

Object = []
Type = []
Material = []
MatSum = []
MatT = []

for obj in bpy.data.objects:
    Object.append(obj.name)
    Type.append(obj.type)
    if len(obj.material_slots) == 0:
        Material.append('None')
        MatSum.append('None')
    else:
        MatSum.append(len(obj.material_slots))
        s_m = ''
        for slot in obj.material_slots:
            s_m = slot.material.name + ',' + s_m
            MatT.append(slot.material.name)
        Material.append(s_m)
            
#for m in MatT:
#    m = bpy.data.materials.get(m)
#    for node in m.node_tree.nodes:
#        if node.type == 'TEX_IMAGE':
#            img = node.image
#            print(img.name)
    
#print(Object)
#print(Type)
#print(Material)
#print(MatT)

dict = {'object': Object, 'type': Type, 'material': Material, 'material number': MatSum}
df = pd.DataFrame(dict)
# save to csv
df.to_csv('/Users/yuanqihu/Library/CloudStorage/OneDrive-PennO365/2025Fall/EDUC5913/MyEDUC-repo/BlenderAPI_test/site.csv')

print("======================================")
df = pd.read_csv('/Users/yuanqihu/Library/CloudStorage/OneDrive-PennO365/2025Fall/EDUC5913/MyEDUC-repo/BlenderAPI_test/site.csv')
# Display the first 5 rows of the data
print(df.head())
# Show basic information about the dataset such as dimensions, data types
print(df.info())
# Total quantity of materials
print("total number of materials:" + str(df['material number'].sum()))