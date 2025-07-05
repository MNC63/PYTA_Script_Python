#---------written by:----------------------
#-------Fauzan Syabana---------------------
#------zansyabana@gmail.com----------------
#Licensed under MIT License

from functools import partial
import pymel.core as pm
import sys
from pathlib import Path

currentPath = Path(__file__).parent
print(currentPath)
sys.path.append(str(currentPath))

import oneLiner_func as of



class oneLinerWindow(object):

    windowName = "OneLiner"

    def __init__(self):
        self.customKeyList = of.getCustomKeys()

    def show(self):

        if pm.window(self.windowName, q=True, exists=True):
            pm.deleteUI(self.windowName)
            pm.windowPref(self.windowName, remove=True)
        pm.window(self.windowName, s=True, w=300, h=100, rtf=False)

        self.buildUI()

        pm.showWindow()

    def buildUI(self):
        toolTip = 'Character replacement symbols:' \
                  '\n! = old name' \
                  '\n# = numbering based on selection, add more # for more digits' \
                  '\n@ = alphabetical numbering based on selection' \
                  '\n\nFind and replace method:' \
                  '\n"oldName">"newName" (without quotes)' \
                  '\n\nRemove first or last character(s):' \
                  '\n-(amount of characters to remove) = removes specific amounts of characters from last character'\
                  '\n+(amount of characters to remove) = removes specific amounts of characters from first character' \
                  '\n\nAdd these symbols at the end to change the options:' \
                  '\n//(number) = define the start number of numbering from #' \
                  '\n/s = selected only (this is default, you dont have to type this)' \
                  '\n/h = add items from all hierarchy descendants of selected items' \
                  '\n\nAdditional tool:'\
                  '\nadd f: at the start of the text to find objects within desired characters'\
                  '\nadd fe: at the start of the text to find objects that ends with the desired characters'\
                  '\nadd fs: at the start of the text to find objects the starts with the desired scharacters'

        column = pm.columnLayout(cal='center', adj=True)
        pm.separator(h=15, style='none')
        self.rnmInput = pm.textField(ec=self.runFunc, aie=True, w=200, ann=toolTip)
        self.popup = pm.popupMenu()
        for i in self.customKeyList:
            pm.menuItem(p=self.popup, label=i, command=partial(self.runPopup,i))
        pm.separator(h=10, style='none')
        pm.text(label='Hover mouse to text field for tool tips')
        pm.text(label='zansyabana@gmail.com')
        pm.separator(h=10, style='none')

    def runFunc(self,*args):
        self.rnmQ = pm.textField(self.rnmInput, text=True,q=True)
        self.newKey = str(self.rnmQ[1:])
        if self.rnmQ.find('^') != -1:
            pm.menuItem(p=self.popup, label=self.newKey, command=partial(self.runPopup,self.newKey))
            pm.textField(self.rnmInput, e=True, text='')
        of.oneLiner(self.rnmQ)

    def runPopup(self,newName,*args):
        self.rnmQ = newName
        of.oneLiner(self.rnmQ)

if __name__ == "__main__":
    oneLinerWindow().show()
