from flask import Flask, render_template, request,url_for
import requests
from pprint import pprint




# Resetando as variaveis


app = Flask('SummerEltroWeather')

url = 'https://api.hgbrasil.com/weather?key=00764386&city_name=Serra,ES'


@app.route('/')
def index():
    req = requests.get(url).json()
    req = req['results']
    cod_img = req['img_id']
    img = f'http://assets.api.hgbrasil.com/weather/images/{cod_img}.png'
    print("========== BUSCANDO API ==========")
    pprint(req)

    # Json com apenas o primeiro indice da lista
    tempo1 = req["forecast"][0]
    # Retira o primeiro indice
    req["forecast"].pop(0)
    # Pega a lista de json -1 indice
    tempo2 = req["forecast"]
    return render_template("index.html",tempo = req, tempo_img = img, tempo1= tempo1 ,tempo2= tempo2 )




@app.route('/lampada/on')
def lampadaOn():
    return {'lampada': True}

@app.route('/lampada/off')
def lampadaOff():
    return {'lampada': False}


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8080, debug=True )
