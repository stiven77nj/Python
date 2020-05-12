class Coche: # Creando la clase
    # Atributos = Propiedades
    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enMarcha = False
    # Metodos = Comportamiento
    def arrancar(self): # Metodo = Es una funcion que solo pertenece a la clase
        self.enMarcha = True # self.enMarcha = miCoche.enMarcha

    def estado(self):
        if self.enMarcha:
            return print("El coche esta en marcha")
        else:
            return print("El coche esta parado")

miCoche = Coche() # Instanciamos una clase
print("El largo del coche es: ",miCoche.largoChasis)
print("El coche tiene ",miCoche.ruedas," ruedas")
miCoche.arrancar()
print(miCoche.estado())
