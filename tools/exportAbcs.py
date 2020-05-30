import sys
import os
import osUtils
import mayaUtils

def main(assetDir):
    scenes = osUtils.getFilesOfType(assetDir, 'ma')
    for scene in scenes:
        abc = mayaUtils.exportMesh(scene)
        print 'Exported:', abc

if __name__ == '__main__':
    main(sys.argv[-1])
