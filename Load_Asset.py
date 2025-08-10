import unreal


def make_blueprint(package_path: str, asset_name: str):
    """
    Usage example: 
    package_path = "/Game/Blueprints"
    asset_name = "BP_Trebuchet20"
    blueprint = make_blueprint(package_path, asset_name)
    """

    factory = unreal.BlueprintFactory()
    factory.set_editor_property(name="parent_class", value=unreal.Actor)

    asset_tools: unreal.AssetTools = unreal.AssetToolsHelpers.get_asset_tools()

    asset: Object = asset_tools.create_asset(asset_name=asset_name,
                                             package_path=package_path,
                                             asset_class=None,
                                             factory=factory)
    if not isinstance(asset, unreal.Blueprint):
        raise Exception("Failed to create blueprint asset")
    blueprint: unreal.Blueprint = asset  # noqa
    return blueprint

# Tạo blueprint
factory = unreal.BlueprintFactory()
factory.set_editor_property("parent_class", unreal.Actor)
blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset("MyBP", "/Game/Blueprints", None, factory)

# Tạo subobject root
subsystem = unreal.get_engine_subsystem(unreal.SubobjectDataSubsystem)
root_handle = subsystem.k2_gather_subobject_data_for_blueprint(blueprint)[0]

# Add component mới
params = unreal.AddNewSubobjectParams(parent_handle=root_handle, new_class=unreal.StaticMeshComponent, blueprint_context=blueprint)
sub_handle, fail = subsystem.add_new_subobject(params)
subsystem.attach_subobject(root_handle, sub_handle)
subsystem.rename_subobject(sub_handle, unreal.Text("MyMeshComp"))

# Lấy object và gán mesh
sp = unreal.SubobjectDataBlueprintFunctionLibrary
sub_data = sp.get_data(sub_handle)
sub_comp = sp.get_object(sub_data)
asset_mesh = unreal.EditorAssetLibrary.load_asset('/Game/Environments/SM_House')
sub_comp.set_editor_property('static_mesh', asset_mesh)

# Save asset
unreal.EditorAssetLibrary.save_asset(blueprint.get_path_name())

blueprint_path = "/Game/Blueprints/MyBP"
blueprint = unreal.load_asset(blueprint_path)

if not blueprint:
    # Nếu chưa có thì tạo mới
    factory = unreal.BlueprintFactory()
    factory.set_editor_property("parent_class", unreal.Actor)
    blueprint = unreal.AssetToolsHelpers.get_asset_tools().create_asset("MyBP", "/Game/Blueprints", None, factory)
unreal.get_engine_subsystem(
    unreal.SubobjectDataSubsystem)

_, rotating = add_subobject(subsystem=subsystem,
                            blueprint=My_BP,
                            new_class=unreal.RotatingMovementComponent,
                            name="RotatingComponent")
 