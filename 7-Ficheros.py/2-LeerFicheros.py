'''
Leyendo fichero ya existente
'''

fichero = open("Archivo1.txt","rt") # Abrimos el fichero en modo lectura

texto = fichero.read() # Lee el contenido dentro del fichero

print(texto)

fichero.close()
