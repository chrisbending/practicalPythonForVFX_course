import sys
import threading

def repeatIt(waitSecs, fncToRun, repeat):
    ''' repeat process over time
    '''
    ticker = threading.Event()
    ticker.daemon = True

    counter = 0
    while not ticker.wait(waitSecs):
        fncToRun()
        counter += 1

        if counter == repeat:
            sys.exit()
