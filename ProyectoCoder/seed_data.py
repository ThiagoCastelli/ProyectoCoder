from AppCoder.models import Familiar
import datetime

Familiar(nombre="Santiago", fecha_nacimiento= datetime.date(1998, 8, 25), direccion="Constituyente 2020", numero_pasaporte=252627).save()
Familiar(nombre="Isa", fecha_nacimiento= datetime.date(1998, 9, 12), direccion="Constituyente 2020", numero_pasaporte=313243).save()
Familiar(nombre="Joaco", fecha_nacimiento= datetime.date(1999, 11, 18), direccion="Carlos Quijano 75", numero_pasaporte=280219).save()
Familiar(nombre="Vicky", fecha_nacimiento= datetime.date(1998, 3, 3), direccion="Tacuarembo 370", numero_pasaporte=244033).save()

print("Se cargo con éxito los usuarios de pruebas")
