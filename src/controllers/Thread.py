from threading import Timer

def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()



