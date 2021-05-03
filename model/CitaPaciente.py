class CitaPaciente():
    def __init__(self, fecha, hora, descripcion, estado, usuario, doctor = None):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion
        self.estado = estado
        self.usuario = usuario
        self.doctor = doctor