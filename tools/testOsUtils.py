import osUtils

testDir = '/Users/christopherbending/Desktop/'

for data in osUtils.getFilesOfType(testDir, 'text'):
    print data
