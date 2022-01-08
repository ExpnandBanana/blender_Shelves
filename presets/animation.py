import bpy
shelf = bpy.context.scene.shelf_list

shelf.clear()
item_sub_1 = shelf.add()
item_sub_1.name = ''
item_sub_1.button_name = 'Name'
item_sub_1.button_operator = 'test.operator'
item_sub_1.button_icon = 'FUND'
item_sub_1.show_button_name = False
