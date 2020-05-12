class Coche:

    def __init__(self): # Constructor, estado inicial
        self.largoChasis = 250
        self.anchoChasis = 120
        self.__ruedas = 4 # Hacemos la propiedad privada, la encapsulamos
        self.enMarcha = False

    def arrancar(self, arrancamos):
        self.enMarcha = arrancamos
        if self.enMarcha:
            print("El coche esta en marcha")
        else:
            print("El coche esta detenido")

    def estado(self):
        print("El coche tiene ",self.__ruedas," ruedas")
        print("El coche tiene un ancho de ",self.anchoChasis)
        print("El coche tiene un largo de ",self.largoChasis)


print("------- Creamos el primer Objeto --------")
miCoche = Coche()
miCoche.arrancar(True)
miCoche.estado()

print("------- Creamos el segundo Objeto --------")
miCoche2 = Coche()
miCoche2.arrancar(False)
miCoche2.__ruedas = 5 # Modificamos el valor de una propiedad, pero esto no se debe de hacer
miCoche2.estado()
