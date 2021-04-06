import timeit

def startR():
    global start
    start = timeit.default_timer()

def stopR():
    global start
    stop = timeit.default_timer()

    print('Time: ', stop - start)