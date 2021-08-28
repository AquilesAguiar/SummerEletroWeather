from flask import Flask, render_template, request,url_for
import requests
from pprint import pprint
from pyA20.gpio import gpio
from pyA20.gpio import port

led = port.PA12

led2 = port.PA11

print(led2)

gpio.init()

# gpio.setcfg(led, gpio.OUTPUT)

gpio.setcfg(led2, gpio.OUTPUT)

# Resetando as variaveis


app = Flask(__name__)

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


@app.route('/lampada')
def lampada():
    return '''<a class="button" href="{{url_for('lampadaOn')}}">Ligar</a> <br> <a class="button" href="{{url_for('lampadaOff')}}">Desligar</a>'''

@app.route("/api/lampanda")
def lampada_api():
    status = request.args.get("status")

    if not status:
        print("Erro de Rota")
        return "Erro faltando parametros"

    if status == "on":
        print("Ligando a Lampada")
        gpio.output(led, 1)
        return "Lampada Ligada"

    if status == "off":
        print("Desligando a Lampada")
        gpio.output(led, 0)
        return "Lampada Desligada"

@app.route('/lampada/on')
def lampadaOn():
    gpio.output(led, 1)
    return '''LampadaOn <a class="button" href="{{url_for('lampadaOn')}}">Ligar</a> <br> <a class="button" href="{{url_for('lampadaOff')}}">Desligar</a>'''

@app.route('/lampada/off')
def lampadaOff():
    return '''LampadaOff <a class="button" href="{{url_for('lampadaOn')}}">Ligar</a> <br> <a class="button" href="{{url_for('lampadaOff')}}">Desligar</a>'''


if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8080, debug=True )
