import os
import subprocess

def main():
    pyScript = '/Users/christopherbending/Desktop/tutorialTools/utils/nukeGradeUtils.py'
    cdl = '/Users/christopherbending/Desktop/demoGrade.cc'

    parentDir = '/Users/christopherbending/Desktop/footageForGrade'
    imageDirs = [os.path.join(parentDir, dr) for dr in os.listdir(parentDir)]
    for imageDir in imageDirs:
        if os.path.isdir(imageDir):
            cmd = '/Applications/Nuke12.1v2/Nuke12.1v2.app/Contents/MacOS/Nuke12.1 --nc -t %s %s %s' % (pyScript, imageDir, cdl)
            subprocess.call([cmd], shell=True)

main()
