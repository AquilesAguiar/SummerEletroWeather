import json
import os


def JsonReader( pathFile ):
    with open( pathFile , 'r' ) as fileJson:
        return json.load( fileJson )


def getSettingsPath():
    return os.path.join( os.getcwd(),'src','settings', 'settings.json' )

def getJsonDto(tempo, img, tempoProxDias, cor):
    return {
        "tempo" : tempo,
        "tempo_img" : img,
        "tempoProxDias" : tempoProxDias,
        "cor" : f"rgb({cor[0]})"
    }
