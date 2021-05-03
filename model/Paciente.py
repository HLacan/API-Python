class Paciente():
    def __init__(self, nombre, apellido, fecha, genero, usuario, contrasena, telefono, cita = None, compras = None):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.genero = genero
        self.usuario = usuario
        self.contrasena = contrasena
        self.telefono = telefono
        if cita is None:
            cita = []
        self.cita = cita
        if compras is None:
            compras = []
        self.compras = compras