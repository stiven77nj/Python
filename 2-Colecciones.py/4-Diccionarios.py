'''
Diccionarios: -> Es un tipo de colección que sus elementos se almacenan
                 desordenados y con la forma clave:valor donde no pueden
                 haber claves duplicadas.
              -> Un diccionario permite eliminar cualquier entrada.
              -> Al igual que las listas, el diccionario permite modificar los valores.
'''
diccionario = {"azul":"blue","rojo":"red","verde":"green"}

diccionario["amarillo"] = "YELLOW" # -> Agregamos un nuevo elemento

del(diccionario["rojo"]) # -> Eliminamos un elemento poniendo la clave

print(diccionario["azul"]) # -> ponemos la clave para mostrar el elemento que deseamos

diccionario = {"Nicolas":[22,1.64],"Jose":[21,1.75],"Maria":[22,1.50]}
print(diccionario)
print("-----------------------------------------------------------")

equipo = {10:"Paulo Dybala",11:"Douglas Costa",7:"Cristiano Ronaldo"}

print(equipo.get(8,"No existe un jugador con ese numero")) # -> Podemos hacer una exepcion

print(10 in equipo) # -> Hacemos una busqueda en el diccionario

print(equipo.keys()) # -> Imprimos solo la clave de los elementos
print(equipo.values()) # -> Imprimimos los valores de cada clave
print(equipo.items()) # -> Forma de mostrar el la clave y el valor
print(len(equipo)) # -> Cuantos elementos tenemos en el equipo
equipo.clear() # -> Limpiamos el diccionario
print(equipo)
