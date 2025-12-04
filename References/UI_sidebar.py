import bpy  # 导入Blender的Python API模块

class HelloWorldPanel(bpy.types.Panel):
    """创建一个面板，在 3D 视图的侧边栏 (N面板) 中显示"""
    
    # 面板的标签
    bl_label = "Hello World Panel"
    
    # 面板的唯一ID
    bl_idname = "VIEW3D_PT_hello"
    
    # 【修改点1】空间类型改为 3D 视图
    bl_space_type = 'VIEW_3D'
    
    # 【修改点2】区域类型改为 UI (侧边栏)
    bl_region_type = 'UI'
    
    # 【修改点3】定义侧边栏的标签页名称
    # 你可以在这里改成任何你喜欢的名字，比如 "My Addon" 或 "工具箱"
    bl_category = "My Tools"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        # 添加一个判断：只有选中了物体才显示功能，否则提示用户
        if obj:
            row = layout.row()
            row.label(text="Hello world!", icon='WORLD_DATA')

            row = layout.row()
            row.label(text="Active object is: " + obj.name)

            row = layout.row()
            row.prop(obj, "name")

            row = layout.row()
            row.operator("mesh.primitive_cube_add")
        else:
            # 如果没有选中物体，显示提示信息
            layout.label(text="请先选中一个物体", icon="INFO")


def register():
    bpy.utils.register_class(HelloWorldPanel)


def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)


if __name__ == "__main__":
    register()