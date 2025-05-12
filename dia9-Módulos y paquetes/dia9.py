#Un módulo es simplemente un archivo .py que contiene código Python (funciones, clases, variables...).Puedes usar ese módulo en otro archivo usando import.

# import math                  # Importa el módulo completo
# from math import pi          # Importa solo una parte
# from math import *           # Importa todo (NO recomendable)
# import math as m             # Le da un alias

from datetime import timedelta
import random
from datetime import datetime,date

#random sirve para generar datos aleatorios

#print(random.randint(1,10))
print(datetime.now()) # fecha y hora actual
print(date.today()) # solo fecha

#datetime Sirve para trabajar con fechas, horas y tiempos.
hoy = date.today()
mañana = hoy + timedelta(days=1)
print(mañana)


# math Contiene funciones matemáticas avanzadas:

import math
print(math.sqrt(16))  # Raíz cuadrada
print(math.pow(2,3))  # Potencia: 2^3
print(math.pi)  # Constante π


# | Módulo     | Propósito                       | Funciones/Clases comunes                          | Ejemplo de uso                                  |
# | ---------- | ------------------------------- | ------------------------------------------------- | ----------------------------------------------- |
# | `random`   | Generar valores aleatorios      | `randint(a, b)`, `choice(lista)`, `random()`      | `random.randint(1, 100)` → Número entre 1 y 100 |
# | `datetime` | Manejo de fechas y horas        | `datetime.now()`, `date.today()`, `timedelta`     | `datetime.now()` → Fecha y hora actuales        |
# | `math`     | Funciones matemáticas avanzadas | `sqrt(x)`, `pow(x, y)`, `pi`, `ceil()`, `floor()` | `math.sqrt(25)` → 5.0 (raíz cuadrada)           |
