from flask import Flask, render_template, request, redirect, url_for
from config import *
from publicaciones import Publicaciones
from persona import Persona
from bson.objectid import ObjectId
from flask_login import LoginManager,login_required
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
con_bd = Conexion()


#csrf = CSRFProtect()

@app.route('/')
def index():
    print('index')
    personas = con_bd['Personas']
    PersonasRegistradas = personas.find()
    return render_template('login/index.html', personas = PersonasRegistradas)

@app.route('/registro')
def registro():
    return render_template('login/registro.html')

@app.route('/registros', methods=['POST'])
def registros():
    print('registro')
    personas = con_bd['Personas']
    nombre   = request.form['nombre']
    apellido = request.form['apellido']
    nacimiento = request.form['nacimiento']
    usuario = request.form['usuario']
    contraseña = request.form['contraseña']
    correo = request.form['correo']
    carrera = request.form['carrera']
    
    if nombre and apellido and nacimiento and usuario and contraseña and correo and carrera:
        persona = Persona(nombre, apellido, nacimiento, usuario, contraseña, correo,carrera)
        personas.insert_one(persona.formato_doc())
        return render_template('login/index.html')
    else:
        return "error"
    
@app.route('/validar', methods=['POST'])
def validaruser():
    publicacio =con_bd['Personas']
    usuario =request.form['usuario']
    password =request.form['password']
    if usuario and password:
        person =publicacio.find_one({"usuario":usuario, "contraseña":password})
        print(person)
        if person:
            return redirect(url_for('menu'))
        else:
            return redirect(url_for('index'))
        #publicaciones = Publicaciones(publicacion)
        #publicacio.insert_one(publicaciones.format_doc())
        #publicacionesRealizadas =publicacio.find()
        #return render_template('muro/muroinicio.html', personas = publicacionesRealizadas)
    else:
        return"ERROR"

@app.route('/muro')
#@login_required
def menu():
    publicacio = con_bd['Publicaciones']
    print('muro')
    publicacionesRealizadas = publicacio.find()
    return render_template('muro/muroinicio.html', personas=publicacionesRealizadas)


@app.route('/guardar_post', methods=['POST'])
def agregarPost():
    publicacio =con_bd['Publicaciones']
    publicacion =request.form['publicacion']
    if publicacion:
        publicaciones = Publicaciones(publicacion)
        publicacio.insert_one(publicaciones.format_doc())
        publicacionesRealizadas =publicacio.find()
        return render_template('muro/muroinicio.html', personas = publicacionesRealizadas)
    else:
        return"ERROR"

@app.route('/eliminar/<string:id_persona>')
def eliminar(id_persona):
    personas = con_bd['Publicaciones']
    personas.delete_one({'_id':ObjectId(id_persona)})
    return redirect(url_for('menu'))

@app.route('/editar_post/<string:persona_id>',methods=['POST'])
def editar_persona(persona_id):
    publicacio =con_bd['Publicaciones']
    publicacion = request.form['publicacione']
    if publicacion:
        publicacio.update_one({'_id':ObjectId(persona_id)},{'$set':{'post':publicacion}})
        return redirect(url_for('menu'))

    else:
        return 'ERROR'

def error_401(error):
    return render_template('login/index.html')

def error_404(error):
    return "Página No Encontrada",404

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')
    

if __name__ == '__main__':
    #csrf.init_app(app)
    app.register_error_handler(401,error_401)
    app.register_error_handler(404,error_404)
    app.run(debug=True, port=1598)