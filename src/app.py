from flask import Flask, render_template, request
from controllers.TempoController import TempoController
from controllers.JsonController import getSettingsPath, JsonReader, getJsonDto, getDatabasePath, JsonSave
from controllers.Thread import setInterval
from controllers.MainController import busca_atualiza_info_led, inicializacao
import platform, os, time

IS_LINUX = platform.system().lower() != "windows"

if IS_LINUX:
    from controllers.LedController import executarFita, setFitaAllColor, setColorArray

if 'root' in os.getcwd():
    temp_folder = os.path.join( os.getcwd(), '..','home', 'projeto', 'SummerEletroWeather','src','templates' )
    static_folder = os.path.join( os.getcwd(), '..','home', 'projeto', 'SummerEletroWeather','src','static' )
else:
    temp_folder = os.path.join( os.getcwd(),'src','templates' )
    static_folder = os.path.join( os.getcwd(),'src','static' )

app = Flask(
        'SummerEltroWeather',
        template_folder = temp_folder ,
        static_folder = static_folder
    )

# Sempre que for inicializar ligando na tomada
# ira iniciar no modo clima e ligado
print("Inicializando aplicação")
inicializacao()

# Aguarda um tempo devido a função de baixo executar em uma thread
print("Aguardando um tempinho")
time.sleep(2)

# 2 em 2 minutos a trhead do python atualiza a informação do tempo na fita led
print("Iniciando a trhead")
setInterval(20.0, busca_atualiza_info_led)

@app.route('/')
def index():
    try:
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
            if IS_LINUX:
                setColorArray(arrayColor)

        tempoProxDias = clima.getProxTempoImg(settingsCondicao)

        database['internet'] = True
        JsonSave(getDatabasePath(), database)

        if request.args.get('type'):
            return getJsonDto(tempo, img, tempoProxDias, cor)
        if request.args.get('reset'):
            return { "ok" : True }

        cor = settingsColors[ tempo['condition_slug'] ]
        return render_template("index.html", tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias, cor = f"rgb({cor[0]})")
    except:
        print("Erro de requisição, esta sem internet.")
        print("Erro de requisição, faltando intenret")
        database = JsonReader( getDatabasePath() )
        database['internet'] = False
        JsonSave(getDatabasePath(), database)
        return render_template("error.html")

@app.route( '/mudaLuz', methods=['POST'] )
def mudaLuz():
    dados = request.get_json()
    JsonCor = JsonReader( getSettingsPath() )["CORES_LEDS"][dados][0].split(',')
    arrayColor = list(map(lambda num: int(num), JsonCor ) )

    database = JsonReader( getDatabasePath() )
    if database['estado']:
        database['cor_atual'] = arrayColor
        JsonSave(getDatabasePath(), database)

        if IS_LINUX:
            setColorArray(arrayColor)

    return {'arrayColor': arrayColor }

@app.route( '/atualizaLocalizacao', methods=['POST'] )
def atualizaLocalizacao():
    dados = request.get_json()
    database = JsonReader(getDatabasePath())
    database["localizacao"] = dados['cidade']+','+dados['estado'].upper()
    JsonSave(getDatabasePath(), database)
    return {'novaLoc':dados}

@app.route( '/lampada/estado', methods=['POST'] )
def lampadaEstado():
    estado = request.get_json().get('estado')

    if estado != None:
        database = JsonReader( getDatabasePath() )
        database['estado'] = estado
        JsonSave(getDatabasePath(), database)

        if IS_LINUX:
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
        database['app'] = not modo
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

            if IS_LINUX:
                setColorArray(arrayColor)

    return {'arrayColor': arrayColor }


if __name__ == '__main__':
    if IS_LINUX:
        app.run( host='0.0.0.0', port=8080 )
    else:
        app.run()
