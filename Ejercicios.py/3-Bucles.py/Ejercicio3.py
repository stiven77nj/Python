'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla
si es un número primo o no.
'''
n = int(input("\nIngrese un numero: "))
cont = 0

for i in range(1,n+1):
    if (n % i) == 0:
        cont += 1

if cont == 2:
    print("\nEl numero es primo")
else:
    print("\nEl numero no es primo")
