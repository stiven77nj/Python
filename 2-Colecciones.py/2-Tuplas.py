'''
Tuplas: -> Son otro tipo de colección que se utilizan principalmente
           para asegurarnos que al terminar de crearlas, los datos no se puedan modificar.
        -> Podemos realizar algunas operacion como en las listas, pero no podemos agregar elementos.
        -> Permite almacenar diferentes tipos de datos.
        -> Usamos () para crear tuplas.
'''

mi_tupla = ("Cadena de texto", 15, 2.8, True)
print(mi_tupla[1]) # Podemos accerder a los elementos ingresando su indice.
print(mi_tupla[0:2]) # Podemos accerder a una porcion de la tupla.
print(mi_tupla[-1]) # Podemos acceder al final de la tupla.
lista = list(mi_tupla) # -> transformamos una tupla en una lista
print(lista)
tupla = tuple(lista) # -> transformamos una lista en una tupla
print(tupla)
