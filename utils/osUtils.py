import os
import tarfile
import glob

def getFilesOfType(destinationDir, fileType):
    """ return files of given type in a location
    """
    fils = []
    for x in os.walk(destinationDir):
        for y in glob.glob(os.path.join(x[0], '*.%s' % fileType)):
            fils.append(y)
    return fils

def rename(dirName, text, mode, replaceText=''):
    """ rename files
    """
    for fil in os.listdir(dirName):
        fil = os.path.join(dirName, fil)
        fileName = os.path.basename(fil)

        if mode == 'prepend':
            newName = os.path.join(dirName, fileName.replace(fileName, text + fileName))
        elif mode == 'replace':
            newName = os.path.join(dirName, fileName.replace(text, replaceText))

        os.rename(fil, newName)
