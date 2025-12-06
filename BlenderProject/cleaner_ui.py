# 导入Blender的Python API模块
import bpy, csv
import pandas as pd


class MTtoCSV(bpy.types.Operator):
    bl_idname = "my_operator.mt_to_csv"
    bl_label = "Models' info to CSV"
    bl_description = "Exporting models' information to csv file."
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        # 只要场景不为空，就允许点击，即满足条件时返回True
        return len(bpy.data.objects) > 0

    # 执行的主程序
    def execute(self, context):
        Object = []
        Type = []
        Material = []
        MatSum = []
        MatT = []

        # 遍历场景中所有对象
        for obj in bpy.data.objects: 
            # 依次添加对象名字
            Object.append(obj.name)
            # 依次添加对象类别
            Type.append(obj.type)
            # 判断对象是否有材质，如果没有则直接依次写入none
            if len(obj.material_slots) == 0:
                Material.append('None')
                MatSum.append('None')
            else:
                # 依次写入对象的材质数量
                MatSum.append(len(obj.material_slots))
                s_m = ''
                # 读取一个对象的每个材质
                for slot in obj.material_slots:
                    s_m = slot.material.name + ',' + s_m
                    MatT.append(slot.material.name)
                # 将所有材质写入，并清理尾部逗号
                Material.append(s_m.rstrip(','))

        dict = {'object': Object, 'type': Type, 'material': Material, 'material number': MatSum}
        df = pd.DataFrame(dict)
        # save to csv
        df.to_csv('/Users/yuanqihu/Library/CloudStorage/OneDrive-PennO365/2025Fall/EDUC5913/MyEDUC-repo/BlenderProject/secene_content.csv')
        
        return {"FINISHED"}


class MTclean(bpy.types.Operator):
    bl_idname = "my_operator.mt_cleaner"
    bl_label = "Material and Texture cleaner"
    bl_description = "A tool to help cleaning redundant materials or textures."
    bl_options = {"REGISTER"}

    @classmethod
    def poll(cls, context):
        return len(bpy.data.materials) > 0

    def execute(self, context):
        deleted_count = 0
        for mat in bpy.data.materials:
            # 判断材质的用户数量（即被对象使用的次数），如果 mat.users == 0，则该材质未被任何对象使用
            if mat.users == 0:
                # 删除该材质，do_unlink=True 会尝试解除所有链接。
                bpy.data.materials.remove(mat, do_unlink=True)
                deleted_count += 1

        # 在 Blender 界面左下角显示结果
        self.report({'INFO'}, f"清理完成。共删除 {deleted_count} 个未使用的材质。")
        return {"FINISHED"}


#创建一个面板，在 3D 视图的侧边栏 (N面板) 中显示
class MTCleaner_ui(bpy.types.Panel):
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

        layout.label(text = "------- 数据导出 -------")
        row = layout.row()
        row.operator(MTtoCSV.bl_idname) # 调用上面的执行函数

        layout.separator()

        layout.label(text = "------- 场景清理 -------")
        row = layout.row()
        row.operator(MTclean.bl_idname) # 调用上面的执行函数


# 注册类和面板的函数
def register():
    bpy.utils.register_class(MTtoCSV)
    bpy.utils.register_class(MTclean)
    bpy.utils.register_class(MTCleaner_ui)

# 注销类和面板的函数
def unregister():
    bpy.utils.unregister_class(MTtoCSV)
    bpy.utils.unregister_class(MTclean)
    bpy.utils.unregister_class(MTCleaner_ui)

# 这部分代码确保如果脚本直接执行，面板会被注册
if __name__ == "__main__":
    register()