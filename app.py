from flask import Flask, render_template, request
import requests

app = Flask(__name__)

url = 'https://api.hgbrasil.com/weather?key=00764386&user_ip=remote'

@app.route('/')
def index():
    req = requests.get(url).json()
    req = req['results']
    return render_template("index.html",tempo = req)



@app.route('/api/lampada')
def lampada():
    return "Lampada"


if __name__ == '__main__':
    app.run(debug=True,use_reloader=True)
