#USAR MODULOS

import datetime
hoy = datetime.date.today()
print(hoy)

from datetime import date
hoy2 = date.today()
print(hoy2)

import time
estampatemporal = time.time()
print(estampatemporal)

from time import time
estampatemporal2 = time()
print(estampatemporal2) 

import validador
from validador import validateEmail

email='pruebapruebacom'
if validateEmail(email):
 print('El correo esta bien escrito')
else:
 print('EL correo esta incorrecto')


#Administrador pra instalar mo
