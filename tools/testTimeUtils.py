import time
import timeUtils
from datetime import datetime

def printIt():
    print time.ctime()

delay = datetime(2020, 5, 9, 16, 48)
while datetime.now() < delay:
    time.sleep(5)

print 'now start', time.ctime()

timeUtils.repeatIt(4, printIt, 5)
