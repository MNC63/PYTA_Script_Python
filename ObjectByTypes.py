import maya.cmds as cmds

object_types = {
    "Meshes": "mesh",
    "Lights": "light",
    "Cameras": "camera",
    "Locators": "locator",
    "NURBS_Curves": "nurbsCurve",
    "NURBS_Surfaces": "nurbsSurface"
}


for group_name, obj_type in object_types.items():
    objs = cmds.ls(type=obj_type)
    if objs:
        group = cmds.group(em=True, name=group_name + "_grp")
        for obj in objs:
            parent = cmds.listRelatives(obj, parent=True, path=True)
            if parent:
                try:
                    cmds.parent(parent[0], group)
                except:

                    pass
