'''
Posicionando un puntero en el fichero
'''

fichero = open("Archivo1.txt","rt")

print(fichero.read())

fichero.seek(0) # Posicionamos el puntero en la poscicion indicada

 print("\n",fichero.read()) # Si ponemos un numero en read(11), se lee el fichero hasta la poscicion dada
