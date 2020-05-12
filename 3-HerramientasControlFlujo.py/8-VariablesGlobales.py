'''
Las variables locales las usamos solamente dentro de una funcion y estas no pueden
modificar a la variables que estan fuera de la funcion.

No podemos llamar a la funcion antes de que la variable global se cree.

No podemos modificar variables globales dentro de una funcion.
'''

def palindromo():
    nuevo_valor = frase.replace(' ','') # Variables locales   # La funcion replace() quita los espacios
    return nuevo_valor == nuevo_valor[::-1]

frase = "anita lava la tina" # Variables globales
print(frase)
resultado = palindromo()
print(frase)
print(resultado)
'''
Para poder modificar el valor de una variable global, usamos la palabra global.
Si una variable no ha sido creada, podemos crear una de tipo global en una funcion
tambien con la palabra global
'''
print("\n")
def valor_global():
    global variable_global  # Modificamos la variable con la plabra global
    variable_global = "Cambiar valor"

def crear_global():
    global nueva_variable # Cramos una variable global
    nueva_variable = "Nueva variable global"

variable_global = "Esto es una variable global"
print(variable_global)
valor_global()
print(variable_global)
crear_global()
print(nueva_variable)
