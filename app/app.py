from flask import Flask, render_template, request,url_for,redirect
from controllers.tempo import Tempo
# from controllers import led

app = Flask('SummerEltroWeather')

@app.route('/')
def index():
    clima = Tempo()
    tempo = clima.getTempo()
    img = clima.getFotoTempo()
    tempoProxDias = clima.getProxTempo()
    return render_template("index.html",tempo = tempo, tempo_img = img, tempoProxDias = tempoProxDias)

@app.route('/lampada/estado',method=['POST'])
def lampadaEstado():
    estadoLampada = request.form['estado'] 
    return {'lampada': True}

@app.route('/lampada/modo',method=['POST'])
def lampadaModo():
    modoLampada = request.form['modo'] 
    return {'lampada': False}

@app.route('/lampada/intesidade',method=['POST'])
def lampadaIntesidade():
    intesidadeLampada = request.form['intesidade']
    return {'lampada': 'forte'}

@app.route('/lampada/mudaCor',method=['POST'])
def lampadaMudaCor():
    mudaCorLampada = request.form['mudaCor']
    return {'lampada': 'cor'}


if __name__ == '__main__':
    app.run(debug=True)
    # app.run( host='0.0.0.0', port=8080, debug=True )
