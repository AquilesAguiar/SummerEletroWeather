from controllers.JsonController import JsonReader, JsonSave, getDatabasePath, getSettingsPath
from controllers.TempoController import TempoController
import platform

IS_LINUX = platform.system().lower() != "windows"

if IS_LINUX:
    print("Carai joao entrei em querer")
    from controllers.LedController import setColorArray

def busca_atualiza_info_led():
    database = JsonReader( getDatabasePath() )
    if database['app'] and database['estado']:
        print("Iniciando Requisição pela Função com a Trhead (❁´◡`❁)")
        settingsJson = JsonReader( getSettingsPath() )
        settingsColors = settingsJson['CORES_LEDS']

        clima = TempoController()
        tempo = clima.getTempo()

        cor = settingsColors[ tempo['condition_slug'] ]
        JsonCor = cor[0].split(',')
        arrayColor = list(map(lambda num: int(num), JsonCor ) )

        if IS_LINUX:
            setColorArray(arrayColor)

    return False


def inicializacao():
    database = JsonReader( getDatabasePath() )
    database['estado'] = True
    database['modo'] = False
    database['app'] = True
    JsonSave(getDatabasePath(), database)
