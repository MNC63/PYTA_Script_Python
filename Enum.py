

# class MedicineColor(Enum):
#     RED_PILL = auto()  # first member
#     BLUE_PILL = auto()  # second member
# # first define enum: using class


# def take_medicine(option: MedicineColor):
#     if option == MedicineColor.RED_PILL:
#         print("You take the red pill and stay in Wonderland.")
#     elif option == MedicineColor.BLUE_PILL:
#         print("You take the blue pill and wake up in your bed.")
# # demo use enum


# take_medicine(MedicineColor.RED_PILL)
from enum import Enum, auto


class Shader_Type(Enum):
    VERTEX = auto()
    FRAGMENT = auto()
    GEOMETRY = auto()
    COMPUTE = auto()


def describe_shader(shader: Shader_Type):
    if shader == Shader_Type.VERTEX:
        print("Transforms 3D vertices to clip space")
    elif shader == Shader_Type.FRAGMENT:
        print("Calculates the colors")
    elif shader == Shader_Type.GEOMETRY:
        print("Generates new geometry from primitives")
    else:
        print("Performs general-purpose computations on GPU")


describe_shader(Shader_Type.GEOMETRY)
