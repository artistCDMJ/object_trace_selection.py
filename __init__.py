import bpy

class TraceSelection(bpy.types.Operator):
    """Convert gpencil to CURVE"""
    bl_idname = "object.trace_selection" 
                                     
     
    bl_label = "Setup Mirror Canvas"
    bl_options = { 'REGISTER', 'UNDO' }
    
    def execute(self, context):
        
        scene = context.scene
        
                
        bpy.ops.gpencil.convert(type='CURVE', use_timing_data=True)
        bpy.ops.object.select_by_type(type = 'CURVE')
        bpy.context.scene.objects.active = bpy.data.objects["GP_Layer"]
        
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.curve.cyclic_toggle()
        bpy.context.object.data.dimensions = '2D'
        
        bpy.ops.object.editmode_toggle()
        bpy.ops.object.convert(target='MESH')
        bpy.ops.object.editmode_toggle()
        bpy.ops.mesh.select_all(action='TOGGLE')
        
        bpy.ops.mesh.dissolve_faces()

        bpy.ops.uv.project_from_view(camera_bounds=True, correct_aspect=False, scale_to_bounds=False)
        bpy.ops.object.editmode_toggle()
        bpy.ops.paint.texture_paint_toggle()
        bpy.context.scene.tool_settings.image_paint.use_occlude = False
        bpy.context.scene.tool_settings.image_paint.use_backface_culling = False
        bpy.context.scene.tool_settings.image_paint.use_normal_falloff = False
        bpy.context.scene.tool_settings.image_paint.seam_bleed = 0


        
        return {'FINISHED'}
    
    
class TestPanel(bpy.types.Panel):
    """A custom panel in the viewport toolbar"""
    bl_label = "Test Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "Tests"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        
        row.label(text="Test Panel")
        
        row = layout.row()
        row.operator("object.trace_selection", text = "Mask from Gpencil", icon = 'ERROR')
            





def register():
    bpy.utils.register_class(TraceSelection)
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(TraceSelection)
    bpy.utils.unregister_class(TraceSelection)
    
    
       
if __name__ == "__main__":
    register()
