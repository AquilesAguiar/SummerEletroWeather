from flask import Flask, render_template, request,url_for
import requests

app = Flask(__name__)

url = 'https://api.hgbrasil.com/weather?key=00764386&city_name=Serra,ES'


@app.route('/')
def index():
    req = requests.get(url).json()
    req = req['results']
    cod_img = req['img_id']
    img = f'http://assets.api.hgbrasil.com/weather/images/{cod_img}.png'

    # Json com apenas o primeiro indice da lista
    tempo1 = req["forecast"][0]
    # Retira o primeiro indice
    req["forecast"].pop(0)
    # Pega a lista de json -1 indice
    tempo2 = req["forecast"]
    return render_template("index.html",tempo = req,tempo_img = img,tempo1=tempo1,tempo2=tempo2)



@app.route('/api/lampada')
def lampada():
    return "Lampada"


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
