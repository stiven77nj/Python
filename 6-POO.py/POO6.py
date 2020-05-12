'''
Polimorfismo
'''
class Coche:
    def desplazamiento(self):
        print("Me desplazo usando cuatro ruedas")


class Moto:
    def desplazamiento(self):
        print("Me desplazo usando dos ruedas")


class Camion:
    def desplazamiento(self):
        print("Me desplazo usando seis ruedas")


def desplazamientoVehiculo(vehiculo): # Pide por parametro un objeto
    vehiculo.desplazamiento()

camion = Camion() # Obejto de tipo Camion
desplazamientoVehiculo(camion)

moto = Moto()
desplazamientoVehiculo(moto)

coche = Coche()
desplazamientoVehiculo(coche)
