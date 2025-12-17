import bpy

# 1. 收集所有被材质使用到的 Image
used_images = set()

for mat in bpy.data.materials:
    if not mat.use_nodes or not mat.node_tree:
        continue
    for node in mat.node_tree.nodes:
        # 常见两类贴图节点：图片贴图 & 环境贴图
        if node.type in {'TEX_IMAGE', 'TEX_ENVIRONMENT'}:
            img = getattr(node, "image", None)
            if img is not None:
                used_images.add(img)

print("被使用的贴图数量：", len(used_images))

# 2. 找出未使用的 Image
unused_images = [img for img in bpy.data.images if img not in used_images]

print("未使用的贴图：")
for img in unused_images:
    print("  ", img.name)

# 3. 如需删除未使用贴图，执行下面这段
#    建议先确认列表无误，再取消注释
for img in unused_images:
    # 如果你不想删除“打了假用户”的，可以先过滤：
    # if img.use_fake_user: continue
    bpy.data.images.remove(img)
