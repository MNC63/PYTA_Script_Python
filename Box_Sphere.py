import unreal

def add_sphere_actor(location, scale=1.0, name="", folder_name=""):
    """
    Thêm một Sphere static mesh actor vào level tại vị trí chỉ định.

    Args:
        location (unreal.Vector): Vị trí để spawn actor.
        scale (float): Tỷ lệ cho sphere. Mặc định là 1.0.
        name (str): Tên của actor.
        folder_name (str): Tên folder để group actor.
    """
    # Tải asset Sphere
    sphere_asset = unreal.EditorAssetLibrary.load_asset('/Engine/BasicShapes/Sphere.Sphere')

    # Tạo actor từ class StaticMeshActor
    actor_class = unreal.StaticMeshActor
    actor_rotation = unreal.Rotator(0.0, 0.0, 0.0)

    # Spawn actor từ class chỉ định
    sphere_actor = unreal.EditorLevelLibrary.spawn_actor_from_class(actor_class, location, actor_rotation)

    # Gán mesh cho actor
    static_mesh_component = sphere_actor.get_component_by_class(unreal.StaticMeshComponent)
    static_mesh_component.set_static_mesh(sphere_asset)

    # Set tỷ lệ của sphere
    sphere_actor.set_actor_scale3d(unreal.Vector(scale, scale, scale))

    # Đặt tên cho actor
    if name:
        sphere_actor.set_actor_label(name)

    # Đặt folder để group actor
    if folder_name:
        sphere_actor.set_folder_path(folder_name)

    return sphere_actor


# Số lượng tổng và số lượng actor trong mỗi group
total_actors = 1000
actors_per_group = 10  # Mỗi group chứa 10 actors

# Đếm số thứ tự cho các actor
actor_counter = 1

# Vòng lặp tạo các Sphere Actors và group chúng
for x in range(10):
    for y in range(10):
        for z in range(10):
            # Tính toán vị trí của mỗi Sphere Actor
            location = unreal.Vector(x * 100.0, y * 100.0, z * 100.0)

            # Đặt tên cho Sphere theo thứ tự từ 1 đến 1000
            actor_name = f"My_Sphere_{actor_counter}"

            # Tên folder (group) mà Sphere sẽ nằm trong
            group_index = (actor_counter - 1) // actors_per_group + 1
            folder_name = f"Sphere_Group_{group_index}"

            # Tạo Sphere Actor với tên, vị trí và folder chỉ định
            add_sphere_actor(location, scale=0.4987, name=actor_name, folder_name=folder_name)

            # Tăng số đếm thứ tự cho actor tiếp theo
            actor_counter += 1

print("Đã tạo xong 1000 Sphere Actors và chia thành 100 nhóm (folders)!")