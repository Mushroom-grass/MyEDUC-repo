import bpy  # 导入Blender的Python API模块

class MyClassName(bpy.types.Operator):
    bl_idname = "my_operator.my_class_name"
    bl_label = "My Class Name"
    bl_description = "Description that shows in blender tooltips"
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        
        return {"FINISHED"}


    bl_idname = "object_data_csv"
    bl_label = "export objects' info to csv"
    def execute(self, context):
        obj = context.object
        self.report({'INFO'}, f"缩放值已报告: ({scale_x:.2f}, {scale_y:.2f}, {scale_z:.2f})")
        return {'FINISHED'} # 操作成功完成

class MTCleaner(bpy.types.Panel):
    #创建一个面板，在 3D 视图的侧边栏 (N面板) 中显示
    # 面板的标签
    bl_label = "Material and Texture Cleaner"
    # 面板的唯一ID
    bl_idname = "VIEW3D_PT_cleaner"
    # 空间类型改为 3D 视图
    bl_space_type = 'VIEW_3D'
    # 区域类型改为 UI (侧边栏)
    bl_region_type = 'UI'
    # 定义侧边栏的标签页名称
    bl_category = "My Cleaner"
    # 这个方法（函数）是 Blender 面板类（继承自 bpy.types.Panel 的类）中最重要的方法。每当 Blender 需要刷新或显示你的自定义面板时，就会调用这个 draw 函数
    def draw(self, context):
        # 取面板的布局(Layout)对象
        layout = self.layout
        # 获取当前在 3D 视图中选中的活动物体 (Active Object)
        obj = context.object

        row = layout.row()
        row.operator(OToCsv.bl_idname) # 调用 "object.report_scale"

        # 添加一个判断：只有选中了物体才显示功能，否则提示用户
        # if obj:
        #     row = layout.row()
        #     row.label(text="Hello world!", icon='WORLD_DATA')

        #     row = layout.row()
        #     row.label(text="Active object is: " + obj.name)

        #     row = layout.row()
        #     row.prop(obj, "name")

        #     row = layout.row()
        #     row.operator("mesh.primitive_cube_add")
        # else:
        #     # 如果没有选中物体，显示提示信息
        #     layout.label(text="请先选中一个物体", icon="INFO")

# 注册类和面板的函数
def register():
    bpy.utils.register_class(MTCleaner)

# 注销类和面板的函数
def unregister():
    bpy.utils.unregister_class(MTCleaner)

# 这部分代码确保如果脚本直接执行，面板会被注册
if __name__ == "__main__":
    register()