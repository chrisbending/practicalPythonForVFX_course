import os
import sys
import time
import imageUtils

update = 10
repeat = 4

path = '/Users/christopherbending/Desktop/ingest'
destDir = '/Users/christopherbending/Desktop'

def watchDir(path):
    print time.ctime()
    return os.stat(path).st_mtime

initCheck = watchDir(path)

startTime = time.time()
counter = 0
while True:
    check = watchDir(path)
    if initCheck != check:
        print 'dir update, run something'
        imageUtils.createProxy(path, destDir, 'jpg')
        initCheck = check

    counter += 1
    if counter == repeat:
        sys.exit()

    time.sleep(update - (time.time()-startTime) % update) # lock in time loop
