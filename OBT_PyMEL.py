import pymel.core as pm

Object_Types = {
    "Meshes": "mesh",
    "Locators": "locator",
    "Cameras": "camera",
    "Lights": "light",
    "NURBS_Curves": "nurbsCurve",
    "NURBS_Surfaces": "nurbsSurface"
}
for group_name, obj_type in Object_Types.items():
    objs = pm.ls(type=obj_type)
    if objs:
        group = pm.group(em=True, name=group_name + "_grp")
        for obj in objs:
            parent = obj.getParent()
            if parent:
                try:
                    pm.parent(parent, group)
                except:
                    pass
