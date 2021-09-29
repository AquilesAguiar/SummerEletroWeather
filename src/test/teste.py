from threading import Timer

def setInterval(timer, task):
    isStop = task()
    if not isStop:
        Timer(timer, setInterval, [timer, task]).start()

def hello():
    print ("do something")
    return False # return True if you want to stop

def buscnado_api():
    print("Buscando API")
    return False

if __name__ == "__main__":
    setInterval(2.0, hello) # every 2 seconds, "do something" will be printed
    print("Vamos entender")
    setInterval(5.0, buscnado_api) # every 2 seconds, "do something" will be printed
    print("Iniciando função de busca de API")
