from model.Paciente import Paciente
from model.Cita import CitaPaciente

paciente = []

paciente.append(Paciente("pacnho","zapato","1","1","3","3","1"))

paciente[0].cita.append(CitaPaciente('31-05-1999','dolores'))

print (paciente[0].nombre)
print (paciente[0].apellido)
print (paciente[0].fecha)
print (paciente[0].genero)
print (paciente[0].usuario)
print (paciente[0].contrasena)
print (paciente[0].telefono)
print (paciente[0].cita[0].fecha)
print (paciente[0].cita[0].descripcion)
print (len(paciente[0].cita))