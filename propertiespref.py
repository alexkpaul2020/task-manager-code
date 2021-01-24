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

def UpdatedFunction(self, context):
    print("In update func...")

class TODOTASK_PG_tasks(PropertyGroup):
    content: StringProperty(
        name="Title",
        default="New Task"
    )

    done: BoolProperty(
        name="Completed",
        default=False,
        update=UpdatedFunction
    )

class TODOTASK_ListSave(PropertyGroup):
    todo_task_list : CollectionProperty(
        type=TODOTASK_PG_tasks
    )

    index : IntProperty(
        name="Selected Todo Task", 
        default=0,   
    )

class TODOTASK_preference(AddonPreferences):
    bl_idname = __package__
    print(bl_idname)
#    topmenu_enabled : BoolProperty(name="Show in 3D View", default=True) 
    n_panel_enabled : BoolProperty(name="Show in Side-Panel", default=True)
    change_name : StringProperty(
        name="", 
        description="button_name",
        default="My Tasks")

    header_enable : BoolProperty(name="Show in Header", default=False)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        c = row.column()
        c.prop(self, "n_panel_enabled")
        c = row.column()
        c.prop(self, "header_enable")
        column = layout.column()
        column.label(text='{}: {}'.format('Task ', 'Change Button Name'))
        column.prop(self, "change_name")
        
classes=[TODOTASK_PG_tasks,
    TODOTASK_ListSave,
    TODOTASK_preference,
    ]
