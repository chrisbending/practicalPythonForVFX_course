import osUtils
import imageUtils

def main(imageDir, fileType, convertTo):
    images = osUtils.getFilesOfType(imageDir, fileType)
    imageUtils.convertImages(images, fileType, convertTo)

if __name__ == '__main__':
    main('/Users/christopherbending/Desktop/footage',  'png', 'jpg')
