'''
Son secuencias de caracteres que forman una busqueda por patron.

Sirven para saber si una cadena de texto tiene el patron buscado.
'''
import re # Importa el modulo de expresiones regulares

texto = "Hola, mi nombre es Nicolas"

resultado = re.search("nombre",texto) # Buscamos la cadena dentro del text
resultado2 = re.search("Nicolas$",texto) # Buscamos si la cadena acaba en esa palabra
resultado3 = re.search("^Hola",texto) # Buscamos si la cadena empieza con esa palabra
resultado4 = re.search("mi.*es",texto) # Buscamos si existen caracter entre esas dos palabras

if resultado:
    print("Cadena encontrada")
else:
    print("Cadena no encontrada")

# Findall -> Busca todas las ocurrencias en una cadena
texto = '''
El coche de luis es rojo
El coche de antonio es blanco
El coche de maria es rojo
'''
resultado = re.findall("coche.*rojo",texto) # Dvuelve una lista con los parametros que le pasamos
print(resultado)

# Split -> divide una cadena a partir de una patro
texto = "La silla es blanca y vale 80"
resultado = re.split("\s",texto) # Divide el texto en las palabras que lo forman
print(resultado)

# Sub -> Sustituye todas las coincidencias de una cadena
texto = "La silla es blanca y vale 80"
resultado = re.sub("blanca","roja",texto) # Cambiamos una palabra por otra
print(resultado)
