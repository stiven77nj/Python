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


class Moto(Vehiculo): # Heredamos de la clase vehiculo
    hcanguro = ''
    def canguro(self):
        self.hcanguro = 'Si, estoy haciendo el canguro'

    def estado(self):
        print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nEn marcha: ",
              self.enMarcha,"\nAcelerando: ",self.acelera,"\nFrenando: ",self.frena,
              "\nHace canguro: ",self.hcanguro)


class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado:
            return print("La furgoneta esta cargada")
        else:
            return print("La furgoneta no esta cargada")


class Electricos(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True


class BiciElectrica(Electricos, Vehiculo): # Herencia multiple, Se hereda el constructor de la clase que esta primero
    pass

print("-------Primer Objeto--------")
moto1 = Moto("KTM","2020")
moto1.canguro()
moto1.estado()
print("-------Segundo Objeto--------")
furgoneta1 = Furgoneta("Renault","Kangoo")
furgoneta1.arrancar()
furgoneta1.estado()
furgoneta1.carga(True)
print("------Tercer Objeto--------")
bici = BiciElectrica("Orbea","Modelo")
