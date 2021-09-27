from flask import Flask, render_template, request, Response
from controllers.TempoController import TempoController
from controllers.JsonController import getSettingsPath, JsonReader, getJsonDto, getDatabasePath, JsonSave
from controllers.LedController import executarFita, setFitaAllColor, setColorArray
import platform, os

app = Flask(
        'SummerEltroWeather',
        template_folder = os.path.join( os.getcwd(),'src','templates' ) ,
        static_folder = os.path.join( os.getcwd(),'src','static' )
    )



@app.route('/')
def index():
    settingsJson = JsonReader( getSettingsPath() )
    settingsCondicao = settingsJson['CONDICOES']
    settingsColors = settingsJson['CORES_LEDS']

    clima = TempoController()
    tempo = clima.getTempo()
    img = clima.getFotoTempo()

    database = JsonReader( getDatabasePath() )
    modo = database['modo']

    if modo:
        arrayColor = database['cor_atual']
    else:
        cor = settingsColors[ tempo['condition_slug'] ]
        JsonCor = cor[0].split(',')
        arrayColor = list(map(lambda num: int(num), JsonCor ) )

    if database['estado']:
        setColorArray(arrayColor)

    tempoProxDias = clima.getProxTempoImg(settingsCondicao)

    if request.args.get('type'):
        return getJsonDto(tempo, img, tempoProxDias, cor)
    if request.args.get('reset'):
        return { "ok" : True }

    return render_template("index.html", tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias, cor = f"rgb({cor[0]})")

@app.route( '/mudaLuz', methods=['POST'] )
def mudaLuz():
    dados = request.get_json()
    JsonCor = JsonReader( getSettingsPath() )["CORES_LEDS"][dados][0].split(',')
    arrayColor = list(map(lambda num: int(num), JsonCor ) )

    database = JsonReader( getDatabasePath() )
    if database['estado']:
        database['cor_atual'] = arrayColor
        JsonSave(getDatabasePath(), database)

        setColorArray(arrayColor)

    return {'arrayColor': arrayColor }



@app.route( '/lampada/estado', methods=['POST'] )
def lampadaEstado():
    estado = request.get_json().get('estado')

    if estado != None:
        database = JsonReader( getDatabasePath() )
        database['estado'] = estado
        JsonSave(getDatabasePath(), database)

        executarFita( setFitaAllColor(0, 0, 0) )

    return {'modo': estado }

@app.route('/database', methods=['POST', 'GET'])
def database():
    database = JsonReader( getDatabasePath() )

    if request.method == "POST":
        estado = request.get_json().get('estado')
        modo = request.get_json().get('modo')
        cor_atual = request.get_json().get('cor_atual')

        if estado != None:
            database['estado'] = estado

        if modo != None:
            database['modo'] = modo

        if cor_atual != None and len(cor_atual) == 3:
            database['cor_atual'] = cor_atual

        JsonSave(getDatabasePath(), database)

        return database

    if request.method == 'GET':
        return database

@app.route( '/lampada/modo', methods=['POST'] )
def lampadaModo():
    modo = request.get_json().get('modo')

    if modo != None:
        database = JsonReader( getDatabasePath() )
        database['modo'] = modo
        JsonSave(getDatabasePath(), database)

    return {'modo': modo }

@app.route( '/lampada/mudaCor', methods=['POST'] )
def lampadaMudaCor():
    arrayColor = request.get_json().get('arrayColor')

    if arrayColor != None:
        database = JsonReader( getDatabasePath() )
        if database['estado']:
            database['cor_atual'] = arrayColor
            JsonSave(getDatabasePath(), database)
            setColorArray(arrayColor)

    return {'arrayColor': arrayColor }


if __name__ == '__main__':
    if platform.system().lower() == "windows":
        app.run( debug=True )
    else:
        app.run( host='0.0.0.0', port=8080, debug=True )
