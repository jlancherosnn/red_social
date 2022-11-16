class Persona:
    def __init__(self, nombre, apellido, nacimiento, usuario, contraseña, correo,carrera):#siempre va self depues los parametros como nombre
        self.nombre = nombre
        self.apellido = apellido
        self.nacimiento = nacimiento
        self.usuario = usuario
        self.contraseña = contraseña
        self.correo = correo
        self.carrera = carrera

    def formato_doc(self):
        return{
            'nombre' : self.nombre,
            'apellido' : self.apellido,
            'nacimiento': self.nacimiento,
            'usuario': self.usuario,
            'contraseña':self.contraseña,
            'correo': self.correo,
            'carrera':self.carrera 
        }