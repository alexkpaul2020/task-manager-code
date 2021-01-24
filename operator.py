import bpy
from bpy.types import (PropertyGroup,
                    Operator,
                    AddonPreferences,
                    Panel,
                    UIList
                    )
from bpy.props import (StringProperty,
                    BoolProperty,
                    CollectionProperty,
                    IntProperty,
                    EnumProperty
                    )

from . import propertiespref

class TODOTASK_OT_AddTask(Operator):
    """Add a new todo item to your list"""

    bl_idname = "todotasks.add"
    bl_label = "Add Item"
    
    target : IntProperty(name="Target Item Index")

    def set_selection(self, n, length):
        return max(max(length, n), 0)
    def execute(self, context):
        list = context.scene.todo_task.todo_task_list
        size = len(list)
        todo = context.scene.todo_task
        
        context.scene.todo_task.todo_task_list.add()
        newindex = self.set_selection(self.target + todo.index, size)
        todo.index = newindex
        return {'FINISHED'}

class TODOTASK_OT_RemoveTask(Operator):
    """Remove the item from your list"""

    bl_idname = "todotasks.remove"
    bl_label = "Remove Item"

    target : IntProperty(name="Target Item Index")

    def execute(self, context):
        cur_index = context.scene.todo_task.index
        if cur_index == self.target:
            context.scene.todo_task.index -= (1 if cur_index > 0 else 0)

        context.scene.todo_task.todo_task_list.remove(self.target)
        return {'FINISHED'}

class TODOTASK_OT_MoveTaskUpDown(Operator):
    """Move the item in your list"""

    bl_idname = "todotasks.move"
    bl_label = "Move Item"

    target : IntProperty(name="Target Item Index")

    direction : EnumProperty(name="Direction", items=[("UP", "Up", "", 1), ("DOWN", "Down", "", 2)])

    def set_selection(self, n, length):
        return max(min(length, n), 0)

    def execute(self, context):
        list = context.scene.todo_task.todo_task_list
        size = len(list)



        if self.direction == "UP":
            todo = context.scene.todo_task
            newindex = self.set_selection(self.target - 1, size)
            list.move(self.target, newindex)
            todo.index = newindex
            
        if self.direction == "DOWN":
            todo = context.scene.todo_task
            newindex = self.set_selection(self.target + 1, size)
            if newindex >=size:
                newindex = self.set_selection(self.target , size)
                list.move(self.target, newindex)
                todo.index = newindex
            else:
                list.move(self.target, newindex)
                todo.index = newindex
        return {'FINISHED'}

class TODOTASK_OT_MoveToBottom(Operator):
    """Move the selected item to the bottom"""

    bl_idname = "todotasks.bottom"
    bl_label = "Move to Last"

    @classmethod
    def poll(cls, context):
        return len(context.scene.todo_task.todo_task_list) > 1

    def execute(self, context):
        todo = context.scene.todo_task
        newindex = len(todo.todo_task_list) - 1
        todo.todo_task_list.move(todo.index, newindex)
        todo.index = newindex
        return {'FINISHED'}

class TODOTASK_OT_MoveToTop(Operator):
    """Move the selected item to the top"""

    bl_idname = "todotasks.top"
    bl_label = "Move to First"

    @classmethod
    def poll(cls, context):
        return len(context.scene.todo_task.todo_task_list) > 1

    def execute(self, context):
        todo = context.scene.todo_task
        todo.todo_task_list.move(todo.index, 0)
        todo.index = 0
        return {'FINISHED'}


classes=[
    TODOTASK_OT_AddTask,
    TODOTASK_OT_RemoveTask,
    TODOTASK_OT_MoveTaskUpDown, 
    TODOTASK_OT_MoveToBottom,
    TODOTASK_OT_MoveToTop
    ]

