'''
Ejercicio 4: Crear un diccionario y mostrar los elementos mediante un ciclo for.
'''

diccionario = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}

print(diccionario)

diccionario["pinia"] = "pineapple"

for clave,valor in diccionario.items():
    print(clave,"->",valor)
