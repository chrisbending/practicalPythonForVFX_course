import os
import argparse
import osUtils

def main():
    """ Run fbx preview generation
    """
    parser = argparse.ArgumentParser(description='find assets and create preview movs')
    parser.add_argument('-d', '--dir', metavar='', default='', help='a dir to find assets')
    parser.add_argument('-a', '--amount', metavar='', default=50, help='set camera distance')
    args = parser.parse_args()

    assetDir = args.dir
    amount = args.amount

    if not assetDir and amount:
        print 'need to supply dir and camera distance'
        return

    for fbx in osUtils.getFilesOfType(assetDir, 'fbx'):
        command =  '/Applications/Houdini/Houdini18.0.287/Frameworks/Houdini.framework/Versions/Current/Resources/bin/'
        command += 'hython -c "import sys; sys.path.append(\'/Users/christopherbending/Desktop/tutorialTools/utils\');'
        command += ' import houUtils; houUtils.captureFbx(\'%s\',\'%s\')"' % (fbx, amount)
        os.system(command)

        dirName = os.path.dirname(fbx)

        # jpeg path
        outputImages = dirName + '/tmp.%04d.jpeg'

        # gen mov
        outputMov = fbx.replace('.fbx', '.mov')
        os.system('/Applications/ffmpeg -r 24 -s 720x720 -i %s %s' % (outputImages, outputMov))

        # del images
        contents= os.listdir(dirName)
        for item in contents:
            if item.endswith('.jpeg'):
                os.remove(os.path.join(dirName, item))

        outputThumbnail = fbx.replace('.fbx', '.jpeg')
        os.system('/Applications/ffmpeg -i %s -vframes 1 -s 360x360 -ss 0.1 %s' % (outputMov, outputThumbnail))

if __name__ == '__main__':
    main()
