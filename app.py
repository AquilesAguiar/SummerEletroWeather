from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def pagina_inicial():
    return render_template("index.html")


@app.route('/api/lampada')
def lampada():
    return "Lampada"


if __name__ == '__main__':
    app.run()
