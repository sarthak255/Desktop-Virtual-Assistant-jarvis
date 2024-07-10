import bpy

# Function to render a 3D scene using Blender with GPU
def render_3d_scene(scene_file, output_file):
    # Ensure Blender uses the GPU for rendering
    bpy.context.preferences.addons['cycles'].preferences.compute_device_type = 'CUDA'
    bpy.context.preferences.addons['cycles'].preferences.get_devices()
    
    for device in bpy.context.preferences.addons['cycles'].preferences.devices:
        device.use = True
    
    # Load the Blender scene
    bpy.ops.wm.open_mainfile(filepath=scene_file)
    
    # Set the output file path
    bpy.context.scene.render.filepath = output_file
    
    # Render the scene
    bpy.ops.render.render(write_still=True)

# Test the 3D rendering function
if __name__ == "__main__":
    render_3d_scene('path_to_blender_scene.blend', 'output_image.png')
