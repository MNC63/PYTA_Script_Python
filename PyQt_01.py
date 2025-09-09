from PySide2 import QtCore
from PySide2 import QtWidgets
from shiboken2 import wrapInstance

import maya.OpenMaya as om
import maya.OpenMayaUI as omui
import maya.cmds as cmds


def maya_main_window():
    """
    Return the Maya main window widget as Python Object
    """
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QWidget)


class MyTool(QtWidgets.QDialog):
    def __init__(self, parent=maya_main_window()):
        super(MyTool, self).__init__(parent)

        # Set window title and size
        self.setWindowTitle("My Tool")
        self.resize(300, 100)

        # UI Element
        self.my_button = QtWidgets.QPushButton("Click me")

        # Layout
        self.my_layout = QtWidgets.QVBoxLayout(self)
        self.my_layout.addWidget(self.my_button)


my_tool = MyTool()
my_tool.show()
