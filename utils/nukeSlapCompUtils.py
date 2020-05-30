import nuke

def main(start, end, fgSeq, bgSeq, newSeq):
   """ Run script
   """
   # open script
   nukeScript = '/Users/christopherbending/Desktop/nukeSlapComp.nknc'
   nuke.scriptOpen(nukeScript)

   # set range
   nuke.knob('root.first_frame', str(start))
   nuke.knob('root.last_frame', str(end))

   # set plates
   nuke.toNode('Read_FG').knob('file').setValue(fgSeq)
   nuke.toNode('Read_FG').knob('first').setValue(int(start))
   nuke.toNode('Read_FG').knob('last').setValue(int(end))

   nuke.toNode('Read_BG').knob('file').setValue(bgSeq)
   nuke.toNode('Read_BG').knob('first').setValue(int(start))
   nuke.toNode('Read_BG').knob('last').setValue(int(end))

   # write result
   nuke.toNode('Write_OUT').knob('file').setValue(newSeq)
   nuke.execute ('Write_OUT', int(start), int(end), 1)

main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
