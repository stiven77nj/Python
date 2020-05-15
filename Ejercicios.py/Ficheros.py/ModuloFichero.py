class Fichero:
    def __init__(self,nombre):
        self.nombre = nombre

    def grabarFichero(self,texto):
        fichero = open(self.nombre,"wt")
        fichero.write(texto)
        fichero.close()

    def incluirFichero(self,texto):
        fichero = open(self.nombre,"at")
        fichero.write(texto)
        fichero.close()

    def leerFichero(self):
        fichero = open(self.nombre,"rt")
        texto = fichero.read()
        return texto
