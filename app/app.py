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
    
    tempoProxDias = req["forecast"]
    
    return render_template("index.html",tempo = req, tempo_img = img, tempoProxDias = tempoProxDias)




@app.route('/lampada/on')
def lampadaOn():
    return {'lampada': True}

@app.route('/lampada/off')
def lampadaOff():
    return {'lampada': False}


if __name__ == '__main__':
    app.run(debug=True)
    # app.run( host='0.0.0.0', port=8080, debug=True )
