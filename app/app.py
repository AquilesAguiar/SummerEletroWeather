from flask import Flask, render_template, request,url_for,redirect
from flask.helpers import make_response
from controllers.tempo import Tempo
from controllers.lerJson import lerJson
import datetime
# from controllers import led

app = Flask('SummerEltroWeather')

@app.route('/')
def index():
    
    jsonCondicao = lerJson("static\json\condicoes.json")
    # jsonCores = lerJson("static\json\coresLed.json")
    clima = Tempo()
    tempo = clima.getTempo()
    img = clima.getFotoTempo()
    condicaoCor = jsonCondicao.lerJson()
    tempoProxDias = clima.getProxTempoImg(condicaoCor)

    red = make_response(render_template("index.html",tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias))
    if request.args.get('type'):
        return {"tempo":tempo, "tempo_img":img, "tempoProxDias":tempoProxDias}
    return red

@app.context_processor
def my_utility_processor():
    def teste():
        jsonCondicao = lerJson("static\json\condicoes.json")
        # jsonCores = lerJson("static\json\coresLed.json")
        clima = Tempo()
        tempo = clima.getTempo()
        img = clima.getFotoTempo()
        condicaoCor = jsonCondicao.lerJson()
        tempoProxDias = clima.getProxTempoImg(condicaoCor)
        return dict(tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias)

    return teste()

@app.route('/lampada/estado',methods=['POST'])
def lampadaEstado():
    estadoLampada = request.get_json()
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
