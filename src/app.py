from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    print('index')
    return render_template('login/index.html')


@app.route('/registro')
def registro():
    print('registro')
    return render_template('login/registro.html')

@app.route('/muro')
def menu():
    print('muro')
    return render_template('muro/muroinicio.html')

if __name__ == '__main__':

    app.run(debug=True, port=1598)