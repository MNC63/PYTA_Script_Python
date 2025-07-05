import unreal


def add_sphere_actor(location, scale=100.0):
    """
    Adds a Sphere static mesh actor to the level at the specified location.

    Args:
        location (unreal.Vector): The location to spawn the actor.
        scale (float): The scale factor for the sphere. Defaults to 100.0.
    """
    # Get the Sphere static mesh asset
    sphere_asset = unreal.load_asset('/Engine/BasicShapes/Sphere')

    # Create the static mesh actor
    actor_class = unreal.StaticMeshActor
    actor_rotation = unreal.Rotator(0.0, 0.0, 0.0)
    sphere_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(
        sphere_asset, location, actor_rotation)

    # Set the scale of the sphere
    sphere_actor.set_actor_scale3d(unreal.Vector(scale, scale, scale))

    return sphere_actor


#location = unreal.Vector(0.0, 0.0, 100.0)
#add one Sphere actor
#sphere_actor = add_sphere_actor(location, scale=49.87)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):      
            location = unreal.Vector(i * 100.0, j * 100.0, k * 100.0)
            sphere_actor = add_sphere_actor(location, scale=0.4987)
    