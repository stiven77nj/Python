class Coche:

    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enMarcha = False

    def arrancar(self, arrancamos):
        self.__enMarcha = arrancamos

        if self.__enMarcha:
            chequeo = self.__chequeoInterno()
        if self.__enMarcha and chequeo:
            return print("El coche esta en marcha")
        elif self.__enMarcha and chequeo == False:
            return print("No podemos arrancar")
        else:
            return print("El coche esta detenido")

    def estado(self):
        print("El coche tiene ",self.__ruedas," ruedas")
        print("El coche tiene un ancho de ",self.__anchoChasis)
        print("El coche tiene un largo de ",self.__largoChasis)

    def __chequeoInterno(self): # Encapsulamos el metodo
        print("Realizando chequeo interno")
        self.gasolina = 'ok' # Creamos una variable
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if (self.gasolina == 'ok') and (self.aceite == 'ok') and (self.puertas == 'cerradas'):
            return True
        else:
            return False


print("------- Creamos el primer Objeto -------")
miCoche = Coche()
miCoche.arrancar(True)
miCoche.estado()

print("------- Creamos el segundo Objeto -------")
miCoche2 = Coche()
miCoche2.arrancar(False)
miCoche2.estado()
