from flask import Flask, render_template, request, redirect, url_for
from config import *
from publicaciones import *
from bson.objectid import ObjectId

app = Flask(__name__)
con_bd = Conexion()



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


@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

##GUARDAR USERS ###################

@app.route('/guaradar_personas', methods=['POST'])
def agregarUser():
    user =con_bd['Personas']
    nombre =request.form['nombre']
    apellido =request.form['apellido']
    nacimiento =request.form['nacimiento']
    usuario =request.form['usuario']
    contraseña =request.form['contraseña']
    correo =request.form['correo']
    carrera =request.form['carrera']
    if nombre and apellido and nacimiento and usuario and contraseña and correo and carrera :
        persona = Personas(nombre,apellido,nacimiento,usuario,contraseña,correo,carrera)
        user.insert_one(persona.format_doc())
        return render_template('login/index.html')
    else:
        return"ERROR"

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

    

if __name__ == '__main__':
    app.run(debug=True, port=1598)