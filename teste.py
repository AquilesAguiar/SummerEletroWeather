try:
    print("Inicializando")
    raise Exception("Mensagem de Error")
    print("Passei")
except Exception as error:
    print("ERROR")
    print(error)
