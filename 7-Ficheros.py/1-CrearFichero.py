'''
Creamos y abrimos el archivo en modo escritura
'''
from io import open

fichero = open("Archivo1.txt","wt") # Cremos el archivo en modo escritura

frase = "Aprendiendo a programar en python" # Añadimos tezto al archivo

fichero.write(frase)

fichero.close()
