import unreal 

class TypeAsset:

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def check_assets(self):
        #Get all assets in folder
        asset_paths = unreal.EditorAssetLibrary.list_assets(self.folder_path, recursive=False)

        for asset_path in asset_paths:
            asset = unreal.EditorAssetLibrary.load_asset(asset_path)

            #Check if this a Type asset what we are looking for (ex: Material Functions)
            if isinstance(asset, unreal.MaterialFunction):
                unreal.log(f"This is Material Function: {asset.get_name()}")
            else:
                unreal.log(f"This is not a Material Function: {asset.get_name()}")

folder_TO_check = "/Game/TypeAsset_Issue"           
checkasset = TypeAsset(folder_TO_check)
checkasset.check_assets()