import Calculadora # No se coloca la extension .py

resultado = Calculadora.suma(30,45)
print(resultado)

'''
Cuando importamos un modulo, python genera un archivo compilado.
Este archivo compilado tiene la extension .pyc

Los archivos compilados hacen que el script se vuelva mas rapido.
Si el archivo no existe, lo crea.
'''

from Calculadora import resta, division # Otra forma de importar

resultado = resta(30,45)
print(resultado)

'''
Podemos renombrar las funcionalidades a importar.
'''
from Calculadora import multiplicacion as mult

resultado = mult(30,45)
print(resultado)
