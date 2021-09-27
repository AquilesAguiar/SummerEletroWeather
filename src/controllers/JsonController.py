import json
import os, json
from sys import path


def JsonSave(pathFile, data):
    with open(pathFile, 'w') as fs:
        json.dump(data, fs, indent=4)

def JsonReader( pathFile ):
    with open( pathFile , 'r' ) as fileJson:
        return json.load( fileJson )

def getSettingsPath():
    return os.path.join( os.getcwd(),'src','settings', 'settings.json' )

def getDatabasePath():
    return os.path.join( os.getcwd(),'src','database', 'database.json' )

def getJsonDto(tempo, img, tempoProxDias, cor):
    return {
        "tempo" : tempo,
        "tempo_img" : img,
        "tempoProxDias" : tempoProxDias,
        "cor" : f"rgb({cor[0]})"
    }
