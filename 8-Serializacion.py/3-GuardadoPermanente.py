import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Persona nueva: ",self.nombre)

    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad)


class ListaPersonas:

    personas = []

    def __init__(self):
        listaDePersonas = open("FicheroExterno","ab+")
        listaDePersonas.seek(0)

        try:
            self.personas = pickle.load(listaDePersonas)
            print("Se cargaron {} personas".format(len(self.personas)))
        except:
            print("El fichero esta vacio")
        finally:
            listaDePersonas.close()
            del (listaDePersonas)

    def agregarPersonas(self, p):
        self.personas.append(p)
        self.guardarPersonas()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)

    def guardarPersonas(self):
        listaDePersonas = open("FicheroExterno","wb")
        pickle.dump(self.personas,listaDePersonas)
        listaDePersonas.close()
        del (listaDePersonas)

    def mostrarFichero(self):
        print("La informacion del fichero es: ")
        for p in self.personas:
            print(p)


lista = ListaPersonas()

p1 = Persona("Ana","Femenino",22)
lista.agregarPersonas(p1)

print("\n")
lista.mostrarFichero()
