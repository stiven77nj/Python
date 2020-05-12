import pickle

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enMarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enMarcha = True

    def acelerar(self):
        self.acelera = True

    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",
              self.enMarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena)

coche1 = Vehiculo("Mazda","MXS")
coche2 = Vehiculo("Seat","Leon")
coche3 = Vehiculo("Renault","Megane")

coches = [coche1,coche2,coche3]

fichero = open("Coches","wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

ficheroApertura = open("Coches","rb")

miscoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in miscoches:
    c.estado()
    print("\n")
