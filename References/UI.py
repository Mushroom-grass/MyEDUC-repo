import bpy  # 导入Blender的Python API模块


# 定义一个自定义面板类 HelloWorldPanel，继承自 bpy.types.Panel
class HelloWorldPanel(bpy.types.Panel):
    """创建一个面板，在 '对象属性' 窗口中显示"""
    
    # 面板的标签，会显示在Blender UI中
    bl_label = "Hello World Panel"
    
    # 面板的唯一ID，用于Blender内部识别
    bl_idname = "OBJECT_PT_hello"
    
    # 面板显示的空间类型，这里是 'PROPERTIES'，即对象属性窗口
    bl_space_type = 'PROPERTIES'
    
    # 面板显示的区域类型，这里是 'WINDOW'，表示在窗口区域显示
    bl_region_type = 'WINDOW'
    
    # 面板显示的上下文，这里是 'object'，即与对象相关的上下文
    bl_context = "object"

    # 面板的绘制方法，这个方法会在面板中绘制UI元素
    def draw(self, context):
        layout = self.layout  # 获取面板的布局对象，用于在面板中添加控件

        obj = context.object  # 获取当前选中的活动对象

        # 创建一行（row），并在其中添加一个标签，显示 "Hello world!" 并使用 'WORLD_DATA' 图标
        row = layout.row()
        row.label(text="Hello world!", icon='WORLD_DATA')

        # 创建新的一行，显示当前活动对象的名称
        row = layout.row()
        row.label(text="Active object is: " + obj.name)

        # 创建新的一行，添加一个控件，让用户可以编辑活动对象的名称
        row = layout.row()
        row.prop(obj, "name")  # 添加一个属性控件，允许修改对象的 'name' 属性

        # 创建新的一行，添加一个操作按钮，点击时会添加一个立方体到场景中
        row = layout.row()
        row.operator("mesh.primitive_cube_add")  # 这个操作会添加一个立方体到当前场景


# 注册类和面板的函数
def register():
    bpy.utils.register_class(HelloWorldPanel)  # 注册 HelloWorldPanel 面板类


# 注销类和面板的函数
def unregister():
    bpy.utils.unregister_class(HelloWorldPanel)  # 注销 HelloWorldPanel 面板类


# 这部分代码确保如果脚本直接执行时，面板会被注册
if __name__ == "__main__":
    register()  # 注册面板
 