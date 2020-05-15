import ModuloFichero

nombreFichero = "Fichero1.txt"
fichero = ModuloFichero.Fichero(nombreFichero)

texto = 'Esta la primera fila del fichero.\nEsta la segubda fila del fichero'
fichero.grabarFichero(texto)

texto = '\nEste es un texto incluido en la tercera fila'
fichero.incluirFichero(texto)

texto_leido = fichero.leerFichero()
print(texto_leido)


 
