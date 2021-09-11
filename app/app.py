from flask import Flask, render_template, request
from controllers.tempo import Tempo
from controllers.lerJson import lerJson
import os, platform
# from controllers.led import led, estado_led

app = Flask('SummerEltroWeather')

@app.route('/')
def index():
    if platform.system().lower() == "windows":
        jsonCondicao = lerJson( os.getcwd() + '\\static\\json\\condicoes.json' )
        jsonCores = lerJson( os.getcwd() +'\\static\\json\\coresLed.json' )
    else:
        jsonCondicao = lerJson( os.getcwd() + '\static\json\condicoes.json' )
        jsonCores = lerJson( os.getcwd() +'\static\json\coresLed.json' )

    clima = Tempo()
    tempo = clima.getTempo()
    img = clima.getFotoTempo()

    condicaoCor = jsonCondicao.lerJson()
    cor = jsonCores.lerJson()
    cor = cor[tempo['condition_slug']]
    tempoProxDias = clima.getProxTempoImg(condicaoCor)
    if request.args.get('type'):
        return {"tempo":tempo, "tempo_img":img, "tempoProxDias":tempoProxDias,"cor":'rgb('+cor[0]+')'}
    return render_template("index.html", tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias,cor='rgb('+cor[0]+')')


@app.route('/mudaLuz',methods=['POST'])
def mudaLuz():
    dados = request.get_json()
    return {"true":True}

@app.route('/lampada/estado', methods=['POST'])
def lampadaEstado():
    estadoLampada = request.get_json()
    # estado_led(estadoLampada)
    print(estadoLampada)
    return {'lampada': True}

@app.route('/lampada/modo',methods=['POST'])
def lampadaModo():
    modoLampada = request.get_json()
    print(modoLampada)
    return {'lampada': False}

@app.route('/lampada/intesidade',methods=['POST'])
def lampadaIntesidade():
    intesidadeLampada = request.get_json()
    print(intesidadeLampada)
    return {'lampada': 'forte'}

@app.route('/lampada/mudaCor',methods=['POST'])
def lampadaMudaCor():
    mudaCorLampada = request.get_json()
    print(mudaCorLampada)
    return {'lampada': 'cor'}


if __name__ == '__main__':
    app.run(debug=True)
    # app.run( host='0.0.0.0', port=8080, debug=True )
