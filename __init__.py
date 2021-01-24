# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "To-do Task",
    "author" : "Alex Paul",
    "description" : "A Daily Task Manager Addon",
    "blender" : (2, 83, 0),
    "version" : (1, 0, 0),
    "location" : "View3D - menu",
    "tracker_url" : "https://github.com/alexkp98/TODO-Task-Manager/issues",
    "category" : "3D View"
}
import bpy
from bpy.types import (PropertyGroup,
                    Operator,
                    AddonPreferences,
                    Panel,
                    UIList,
                    Scene,
                    VIEW3D_MT_editor_menus,
                    TOPBAR_HT_upper_bar
                    )
from bpy.props import (StringProperty,
                    BoolProperty,
                    CollectionProperty,
                    IntProperty,
                    EnumProperty
                    )
# from .TodoTask import TODOTASK_ListSave, classes, view_panel_draw

from .propertiespref import (classes, TODOTASK_ListSave)
from .operator import classes
from .ui import (
                classes,
                view_panel_draw,
                draw_button
                )

classes=[
    ui.TODOTASK_UL_Task,
    ui.TODOTASK_PT_NPanel,
    ui.TODOTASK_PT_3DPanel,
    operator.TODOTASK_OT_AddTask,
    operator.TODOTASK_OT_RemoveTask,
    operator.TODOTASK_OT_MoveTaskUpDown, 
    operator.TODOTASK_OT_MoveToBottom,
    operator.TODOTASK_OT_MoveToTop,
    propertiespref.TODOTASK_PG_tasks,
    propertiespref.TODOTASK_ListSave,
    propertiespref.TODOTASK_preference,
    
    ]

def register():
    for cls in classes:

        bpy.utils.register_class(cls)
    Scene.todo_task = bpy.props.PointerProperty(name="To-do Task",type=TODOTASK_ListSave)
    VIEW3D_MT_editor_menus.append(view_panel_draw)
    TOPBAR_HT_upper_bar.prepend(draw_button)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    VIEW3D_MT_editor_menus.remove(view_panel_draw)
    TOPBAR_HT_upper_bar.remove(draw_button)
    del Scene.todo_task


