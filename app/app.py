from flask import Flask, render_template, request,url_for,redirect
from controllers.tempo import Tempo
from controllers.lerJson import lerJson
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
    return render_template("index.html",tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias)


@app.route('/lampada/estado',methods=['POST'])
def lampadaEstado():
    estadoLampada = request.get_json()
    return {'lampada': True}

@app.route('/lampada/modo',methods=['POST'])
def lampadaModo():
    modoLampada = request.get_json()
    return {'lampada': False}

@app.route('/lampada/intesidade',methods=['POST'])
def lampadaIntesidade():
    intesidadeLampada = request.get_json()
    return {'lampada': 'forte'}

@app.route('/lampada/mudaCor',methods=['POST'])
def lampadaMudaCor():
    mudaCorLampada = request.get_json()
    print(mudaCorLampada)
    return {'lampada': 'cor'}


if __name__ == '__main__':
    app.run(debug=True)
    # app.run( host='0.0.0.0', port=8080, debug=True )
