'''
while: Permite ejecutar una misma accion "mientra que" una determinada condicion
se cumpla.
'''

import math

n = int(input("Digite un numero: "))

while n < 0:
    print("Digite un numero positivo")
    n = int(input("Digite un numero: "))

print(f"\nLa raiz cuadrada del numero es: {(math.sqrt(n))}")
