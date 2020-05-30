import sys
import re
import osUtils
import nuke

def main(imageDir, cdl):
   """ Run script
   """
   # open script
   nukeScript = '/Users/christopherbending/Desktop/gradeDemo.nknc'
   nuke.scriptOpen(nukeScript)

   frames = sorted(osUtils.getFilesOfType(imageDir, 'exr'))
   start = frames[0]
   end = frames[len(frames) - 1]

   seqPath = re.sub('\..*.', '.####', start) + '.exr'
   start = start.split('.')[1]
   end = end.split('.')[1]

   # set range
   nuke.knob('root.first_frame', str(start))
   nuke.knob('root.last_frame', str(end))

   # read plate
   nuke.toNode('Read1').knob('file').setValue(seqPath)
   nuke.toNode('Read1').knob('first').setValue(int(start))
   nuke.toNode('Read1').knob('last').setValue(int(end))

   # add .cc file
   nuke.toNode('OCIOCDLTransform1').knob('file').setValue(cdl)

   # write result
   newSeq = seqPath.replace('.', '_graded.', 1)
   nuke.toNode('Write1').knob('file').setValue(newSeq)
   nuke.execute ('Write1', int(start), int(end), 1)

main(sys.argv[1], sys.argv[2])
