'''
Guarda en un fichero externo una coleccion, un objeto, etc, pero lo guarda en formato
de codigo binario.

Necesitamos la biblioteca pickle para usar los metodos:
1). dump(): Volcado de datos al fichero binario externo.
2). load(): Carga de los datos del fichero binario externo.
'''

import pickle

lista_nombres = ['Nicolas', 'Stiven', 'Roman']

fichero_binario = open("lista_nombres","wb") # Creamos el fichero en formato escritura binaria

pickle.dump(lista_nombres,fichero_binario) # Le pasamos la lista y el fichero que creamos

fichero_binario.close()
