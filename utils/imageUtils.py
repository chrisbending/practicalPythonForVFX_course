from PIL import Image
import os
import osUtils

def convertImages(images, convertFrom, convertTo):
    """ convert one image type to another
    """
    for image in images:
        im = Image.open(image)
        newImage = image.replace(convertFrom, convertTo)
        im.save(newImage)

def convertToTex(images):
    """ convert images to tex
    """
    for image in images:
        txMakeStr = '/Applications/Pixar/RenderManProServer-23.2/bin/txmake'
        txMakeStr += ' -format openexr %s %s' % (image, image.replace('.tif', '.tex'))
        os.system(txMakeStr)

def createProxy(inDir, destDir, fileType):
    """ create proxy images
    """
    for dr in os.listdir(inDir):
        currentDir = os.path.join(inDir, dr)
        if os.path.isdir(currentDir):
            newDir = os.path.join(destDir, os.path.basename(currentDir) + '_proxy')
            if not os.path.exists(newDir):
                os.mkdir(newDir)

            for img in osUtils.getFilesOfType(currentDir, fileType):
                image = Image.open(img)
                size = image.size
                image.thumbnail((size[0]/2, size[1]/2))
                image.save(img.replace(currentDir, newDir))
                
