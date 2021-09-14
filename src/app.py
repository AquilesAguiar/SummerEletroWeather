from flask import Flask, render_template, request
from controllers.TempoController import TempoController
from controllers.JsonController import getSettingsPath, JsonReader, getJsonDto
# from controllers.LedController import estado_led
import platform

app = Flask('SummerEltroWeather')

@app.route('/')
def index():
    settingsJson = JsonReader( getSettingsPath() )
    settingsCondicao = settingsJson['CONDICOES']
    settingsColors = settingsJson['CORES_LEDS']

    clima = TempoController()
    tempo = clima.getTempo()
    img = clima.getFotoTempo()

    cor = settingsColors[ tempo['condition_slug'] ]
    tempoProxDias = clima.getProxTempoImg(settingsCondicao)

    if request.args.get('type'):
        return getJsonDto(tempo, img, tempoProxDias, cor)

    return render_template("index.html", tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias, cor = f"rgb({cor[0]})")


@app.route( '/mudaLuz', methods=['POST'] )
def mudaLuz():
    dados = request.get_json()
    return {"true":True}

@app.route( '/lampada/estado', methods=['POST'] )
def lampadaEstado():
    estadoLampada = request.get_json()
    # estado_led(estadoLampada)
    print(estadoLampada)
    return {'lampada': True}

@app.route( '/lampada/modo', methods=['POST'] )
def lampadaModo():
    modoLampada = request.get_json()
    print(modoLampada)
    return {'lampada': False}

@app.route( '/lampada/intesidade', methods=['POST'] )
def lampadaIntesidade():
    intesidadeLampada = request.get_json()
    print(intesidadeLampada)
    return {'lampada': 'forte'}

@app.route( '/lampada/mudaCor', methods=['POST'] )
def lampadaMudaCor():
    mudaCorLampada = request.get_json()
    print(mudaCorLampada)
    return {'lampada': 'cor'}


if __name__ == '__main__':
    if platform.system().lower() == "windows":
        app.run( debug=True )
    else:
        app.run( host='0.0.0.0', port=8080, debug=True )
