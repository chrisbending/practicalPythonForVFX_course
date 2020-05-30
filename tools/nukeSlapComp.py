import subprocess

def main():
    pyScript = '/Users/christopherbending/Desktop/tutorialTools/utils/nukeSlapCompUtils.py'

    start, end = 1, 20
    fgSeq = '/Users/christopherbending/Desktop/Nuke_FG/fg.####.png'
    bgSeq = '/Users/christopherbending/Desktop/Nuke_BG/bg.####.png'
    newSeq = '/Users/christopherbending/Desktop/Nuke_NEW/tmp.####.png'

    cmd = '/Applications/Nuke12.1v2/Nuke12.1v2.app/Contents/MacOS/Nuke12.1 --nc -t %s %d %d %s %s %s' % (pyScript, start, end, fgSeq, bgSeq, newSeq)
    subprocess.call([cmd], shell=True)

main()
