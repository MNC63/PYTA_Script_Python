from functools import partial
import pymel.core as pm
import json, os
from pathlib import Path
import platform

maya_dir = os.getenv('MAYA_APP_DIR')

customKeyPath = Path(maya_dir)/"scripts/OLUserCustom.txt"



def getCustomKeys():
    customKeys = []
    try:
        with open(customKeyPath,'r') as customKeyHandle:
            for line in customKeyHandle:
                curItem = line[:-1]
                customKeys.append(curItem)
    except:
        customKeyFile = open(customKeyPath, "w")
        customKeyFile.close()
    return customKeys

def addCustomKey(lookName):
    newKey = str(lookName[1:])
    customKeyFile = open(customKeyPath, "a")
    customKeyFile.write('{}\n'.format(newKey))
    customKeyFile.close()
    

#selector
def selector(lookName):
    nameSplit = lookName.split(':')
    method = nameSplit[0]
    nameSel = nameSplit[1]
    if method == 'f':
        sel = pm.ls("*{}*".format(nameSel), r=True)
    elif method == 'fe':
        sel = pm.ls("*{}".format(nameSel), r=True)
    elif method == 'fs':
        sel = pm.ls("{}*".format(nameSel), r=True)
    pm.select(sel)

def oneLiner(nName, method='s'):

    # get selection method
    if nName.find(':') != -1:
        selector(nName)
    elif nName.startswith('^') == True:
        addCustomKey(nName)
    elif nName.find('/s') != -1:
        method = 's'
        nName = nName.replace('/s', '')
    elif nName.find('/h') != -1:
        method = 'h'
        nName = nName.replace('/h', '')
    elif nName.find('/a') != -1:
        if nName.find('>') != -1:
            method = 'a'
            print(method)
        nName = nName.replace('/a', '')

    if method == 's':
        slt = pm.selected()
    elif method == 'h':
        sltH = []
        slt = pm.selected()
        for i in slt:
            sltH.append(i)
            for child in reversed(i.listRelatives(ad=True, type='transform')):
                sltH.append(child)
        print(sltH)
        slt = sltH
    elif method == 'a':
        slt = pm.ls()



    # find numbering replacement
    def numReplace(numName, idx, start=1):
        global padding
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if numName.find('//') != -1:
            start = int(numName[numName.find('//') + 2:len(numName)])
            numName = numName.replace(numName[numName.find('//'):len(numName)], '')
            print(start)
        number = idx + start
        if numName.find('#') != -1:
            padding = numName.count('#')
            hastag = "{0:#>{1}}".format("#", padding)  # get how many '#' is in the new name
            num = "{0:0>{1}d}".format(number, padding)  # get number
            numName = numName.replace(hastag, num)
        # alphabetical numbering
        if numName.find('@') != -1:
            padding = numName.count('@')
            aSym = "{0:@>{1}}".format("@", padding) # get how many '@' is in the new name
            alphaNum = "{}".format(alpha[idx])  # get alphabetical number
            numName = numName.replace(aSym, alphaNum)

        return numName
    if nName.find(':') == -1 and nName.find('^') == -1:
        for i in slt:  # for every object in selection list
            # check if there is '>' that represents the replacement method
            if i.name().find('|') !=-1:
                curName = i.name().split('|')[-1]
            else:
                curName = i.name()
            if nName.find('>') != -1:
                wordSplit = nName.split('>')
                oldWord = wordSplit[0]
                newWord = numReplace(wordSplit[1],slt.index(i))
                try:
                    pm.rename(i,i.replace(oldWord,newWord))
                except:
                    print("{} is not renamed".format(i))

            # check if the first character is '-' or '+', remove character method
            elif nName[0] == '-':
                charToRemove = int(nName[1:len(nName)])
                try:
                    pm.rename(i, i[0:-charToRemove])
                except:
                    print("{} is not renamed".format(i))

            elif nName[0] == '+':
                charToRemove = int(nName[1:len(nName)])
                pm.rename(i, i[charToRemove:len(curName)])

            else:
                newName = numReplace(nName, slt.index(i))
                # get current Name if '!' mentioned
                print(i)
                if newName.find('!') != -1:
                    newName = newName.replace('!', curName)
                    print(newName)
                try:
                    pm.rename(i, newName)
                except:
                    print("{} is not renamed".format(i))