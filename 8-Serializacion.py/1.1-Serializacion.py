import pickle

fichero = open("lista_nombres","rb") # Abrimos el fichero binario en modo lectura

lista = pickle.load(fichero) # Cogemos los datos del fichero

print(lista) # Mostramos la lista guardada en el fichero binario
