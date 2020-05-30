import os
import argparse

def main():
    """ Run polyReduceDemo
    """
    parser = argparse.ArgumentParser(description='find assets and polyReduce them by a given amount')
    parser.add_argument('-d', '--dir', metavar='', default='', help='a dir to find assets')
    parser.add_argument('-a', '--amount', metavar='', default=50, help='amount to reduce asset by')
    args = parser.parse_args()

    assetDir = args.dir
    amount = args.amount

    if not assetDir and amount:
        print 'need to supply dir and reduction amount'
        return

    command =  '/Applications/Houdini/Houdini18.0.287/Frameworks/Houdini.framework/Versions/Current/Resources/bin/'
    command += 'hython -c "import sys; sys.path.append(\'/Users/christopherbending/Desktop/tutorialTools/utils\');'
    command += ' import houUtils; houUtils.runReduction(\'%s\',\'%s\')"' % (assetDir, amount)
    os.system(command)

    print 'reduction complete'

if __name__ == '__main__':
    main()
