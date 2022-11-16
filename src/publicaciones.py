class Publicaciones:
    def __init__(self,publicacion):
        self.publicacion = publicacion
    def format_doc(self):
        return {
            'post':self.publicacion
        }

class Personas:
    def __init__(self,nombre,apellido,nacimiento,usuario,contraseña,correo,carrera,):
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.usuario = usuario
        self.contraseña = contraseña
        self.correo = correo
        self.carrera = carrera
    def format_doc(self):
        return {
            'nombre':self.nombre,
            'apellido':self.apellido,
            'nacimiento':self.nacimiento,
            'usuario':self.usuario,
            'contraseña':self.contraseña,
            'correo':self.correo,
            'carrera':self.carrera
        }