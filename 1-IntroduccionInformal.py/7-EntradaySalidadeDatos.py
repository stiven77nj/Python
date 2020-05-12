'''
Para la entrada de datos tenemos:
'''
name = input("Digite su nombre: ") # input guarda datos de tipo cadena
edad = int(input("Digite su edad: ")) # forma de guardar datos de tipo entero
print("\n")
print(f"Su nombre es {nombre} y su edad es {edad} anios")
print("---------------------------------------------------------")
'''
Podemos usar diferentes formas para la salida de datos, por ejemplo:
'''
# Forma 1:
nombre = "Nicolas"
edad = 19
print("Hola",nombre," tienes ",edad," anios de edad")

# Forma 2: Función llamada format()
print("\n")
print("Hola {} tienes {} anios de edad".format(nombre,edad))

# Forma 3:
print("\n")
print(f"Hola {nombre} tienes {edad} anios de edad")
print("\n")
