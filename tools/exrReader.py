import osUtils
import OpenEXR

exrDir = '/Users/christopherbending/Desktop/footage'

exrs = osUtils.getFilesOfType(exrDir, 'exr')

exrObj = OpenEXR.InputFile(exrs[0])

plateData = {}
plateData['width'] = exrObj.header()['nuke/width']
plateData['height'] = exrObj.header()['nuke/height']
plateData['framerate'] = exrObj.header()['nuke/frameRate']
plateData['pixel aspect'] = exrObj.header()['nuke/pixelAspectRatio']
plateData['focus unit'] = exrObj.header()['nuke/focusUnit']
plateData['camera model'] = exrObj.header()['nuke/cameraModel']
plateData['lens model'] = exrObj.header()['nuke/lensModel']
plateData['lens serial no.'] = exrObj.header()['nuke/lensSerialNo']

focalLength = []
focusDistance = []

for img in sorted(exrs):
	exrObj = OpenEXR.InputFile(img)

	focalLength.append(exrObj.header()['nuke/focalLength'])
	focusDistance.append(exrObj.header()['nuke/focalDistance'])

	plateData['focalLengthMin'] = min(focalLength)
	plateData['focalLengthMax'] = max(focalLength)
	plateData['focusDistanceMin'] = min(focusDistance)
	plateData['focusDistanceMax'] = max(focusDistance)

import yaml
with open('/Users/christopherbending/Desktop/shotA_plateInfo.yaml', 'w') as f:
    yaml.dump(plateData, f, default_flow_style=False)
