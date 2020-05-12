import random

valor = random.randint(0,10) # Numero aleatorio del 1 al 10
print(valor)

lista = ['Nicolas', True, 23, 5.2]
valor = random.choice(lista) # Escoge un valor aleatorio de la lista
print(valor)

random.shuffle(lista) # Desordena la lista
print(lista)

import datetime

print(datetime.datetime.now()) # Muestra la hora

import sys
import time

for i in range(100):
    time.sleep(0.5) # Vemos como cambian los numeros
    sys.stdout.write("\r%d %%" % i)
    sys.stdout.flush()
