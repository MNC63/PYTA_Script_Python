import unreal
from pathlib import Path

def import_fbx_with_pathlib(file_path, destination_path):
    """
    Imports an FBX file from the specified file path into the given destination in the Content Browser.

    Args:
        file_path (Path): The file path to the FBX asset on disk using pathlib.
        destination_path (str): The destination path in the Unreal Content Browser (e.g., '/Game/MyFolder').
    """
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

    # Create the import task
    task = unreal.AssetImportTask()
    task.filename = str(file_path)  # Convert pathlib Path to string
    task.destination_path = destination_path
    task.automated = True
    task.save = True  # Automatically save the asset after importing

    # Customize import options (FBX Import settings)
    fbx_import_options = unreal.FbxImportUI()
    fbx_import_options.import_mesh = True  # Import as a static mesh
    fbx_import_options.import_as_skeletal = False  # False for static meshes, True for skeletal meshes
    fbx_import_options.mesh_type_to_import = unreal.FBXImportType.FBXIT_STATIC_MESH  # Set the type of mesh to import
    task.options = fbx_import_options

    # Run the import task
    asset_tools.import_asset_tasks([task])

    # Check if the asset was imported successfully
    if task.imported_object_paths:
        imported_asset_path = task.imported_object_paths[0]
        unreal.log(f"Asset imported successfully: {imported_asset_path}")
        return imported_asset_path
    else:
        unreal.log_error(f"Failed to import asset from: {file_path}")
        return None

# Example usage
fbx_file_path = Path(r"D:\Übung\Nissan 2000 Cartoon\SM_Nissan_2000_cartoon.fbx")
destination_content_path = "/Game/Assets/Car"  # The destination in the Unreal Content Browser
imported_asset = import_fbx_with_pathlib(fbx_file_path, destination_content_path)