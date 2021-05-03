class Doctor():
    def __init__(self, nombre, apellido, fecha, genero, usuario, contrasena, especialidad, telefono, cita = None):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha = fecha
        self.genero = genero
        self.usuario = usuario
        self.contrasena = contrasena
        self.especialidad = especialidad
        self.telefono = telefono
        if cita is None:
            cita = []
        self.cita = cita