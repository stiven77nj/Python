'''
Es una forma de almacenar y cambiar datos que estan en formato texto.
'''
import json

# Covertir datos de una diccionario Python en una estructura JSON
diccionario = {"nombre":"silla", "color":"blanco", "precio":"80"}
estructura = json.dumps(diccionario) # Le pasamos el diccionario y nos devuelve uan estructura json
print(estructura) # Vemos el diccionario pero como una cadena de caracteres, no un diccionario

# Convertir una estructura JSON en un diccionario en Python
resultado2 = json.loads(estructura) # Convierte una estructura json en un diccionario
print(resultado2)
