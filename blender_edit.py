import bpy

object = bpy.data.objects['Plane'] # insert name of desired object

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_mode(type='VERT')
bpy.ops.mesh.select_all(action='SELECT')

bpy.ops.mesh.extrude_region_move(
        TRANSFORM_OT_translate={"value":(0, 0, 3)}
)

bpy.ops.object.mode_set(mode='OBJECT')

modifier = object.modifiers.new(name="Solidify", type='SOLIDIFY')
modifier.thickness = 0.25
