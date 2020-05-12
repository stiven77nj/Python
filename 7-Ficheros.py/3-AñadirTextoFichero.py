'''
Escribimos texto en un archivo ya existente
'''

fichero = open("Archivo1.txt","at") # Abrimos el fichero ya existente para añadir

texto = "\nAgregando mas texto al fichero"

fichero.write(texto)

fichero.close()
