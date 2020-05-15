import pickle

frutas = {"manzana":"apple", "naranja":"orange", "platano":"banana", "limon":"lemon"}
print(frutas)

fichero = open("Fichero2.pckl","wb")
pickle.dump(frutas,fichero)
fichero.close()

leer = open("Fichero2.pckl","rb")
datos = pickle.load(leer)
print(datos)
