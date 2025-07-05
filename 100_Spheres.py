import unreal
def add_sphere_actor(location, scale=100.0, name=None):
    sphere_asset = unreal.load_asset('/Engine/BasicShapes/Sphere')

    # Create the static mesh actor
    actor_rotation = unreal.Rotator(0.0, 0.0, 0.0)
    sphere_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(
        sphere_asset, location, actor_rotation)

    # Set the scale of the sphere
    sphere_actor.set_actor_scale3d(unreal.Vector(scale, scale, scale))

    # Set the name of the actor if provided
    if name:
        sphere_actor.set_actor_label(name)

    return sphere_actor

def spawn_spheres_in_grid(grid_size, offset, scale=100.0, base_name="Sphere_Actor"):
    x_count, y_count, z_count = grid_size
    spheres = []
    for x in range(x_count):
        for y in range(y_count):
            for z in range(z_count):
                location = unreal.Vector(x * offset.x, y * offset.y, z * offset.z)
                name = f"{base_name}_{x}_{y}_{z}"
                sphere_actor = add_sphere_actor(location, scale=scale, name=name)
                spheres.append(sphere_actor)
    return spheres

def move_actors_to_folder(actors, folder_path):
    for actor in actors:
        try:
            actor.set_folder_path(folder_path)
        except Exception as e:
            unreal.log_error(f"Failed to move actor {actor.get_name()} to folder {folder_path}: {str(e)}")

grid_size = (10, 10, 10)  # Create a 10x10x10 grid
offset = unreal.Vector(300.0, 300.0, 300.0)  # Offset each sphere by 300 units in X, Y, and Z
scale = 1
base_name = "MySphere"
folder_path = "Myspheres"  # Folder path in the World Outliner
# Spawn the spheres
spawned_spheres = spawn_spheres_in_grid(grid_size, offset, scale, base_name)
# Move the spawned spheres to folder in the World Outliner
move_actors_to_folder(spawned_spheres, folder_path)