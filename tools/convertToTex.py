import osUtils
import imageUtils
import sys

def main(assetDir):
    if len(sys.argv) != 2:
        print 'no directory provided'
        return

    images = osUtils.getFilesOfType(assetDir, 'tif')
    imageUtils.convertToTex(images)

main(sys.argv[-1])
