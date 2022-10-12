from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    print('index')
    return render_template('index.html')


@app.route('/registro')
def registro():
    print('registro')
    return render_template('registro.html')

@app.route('/muro')
def menu():
    print('muro')
    return render_template('menu.html')

if __name__ == '__main__':

    app.run(debug=True, port=1598)