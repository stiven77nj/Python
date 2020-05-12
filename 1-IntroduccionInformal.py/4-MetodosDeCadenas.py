'''
Metodos de Cadenas:
1). upper() = Convierte letras en mayuscula.
2). lower() = Convierte letras en minuscula.
3). capitalize() = Pone la primera letra en mayuscula.
4). count() = Cuenta cuantas veces aparaece una letra en una cadena.
5). find() = Representa la posicion de un elemento.
6). isdigit() = Dice si el valor es un numero o no.
7). isalum() = Dice si la cadena es alfanumerica.
8). isalpha() = Dice si solo hay letras.
9). split() = Separa por palabras.
10). strip() = Borra los espacios sobrantes al principio y final.
11). replace() = Cambia una letra por otra.
12). rfind() = Representa el indice de un caracter comenzando desde atras.
'''
cadena = "Programando"
cadena2 = "python"

resultado = "{} en {}".format(cadena,cadena2) # Utilizando format()
print(resultado)
resultado2 = "{a} en {b}".format(a = cadena,b = cadena2) # Utilizando format()
print(resultado2)
print("----------------------------")
print(resultado.lower()) # Convierte todo en minuscula
print(resultado.upper()) # Convierte todo a mayuscula
print("----------------------------")
print(resultado.title()) # Convierte la cadena como un titulo
print("----------------------------")
pos = resultado.find("P") # Buscando en donde se ecuentra un caracter
print(pos)
count = resultado.count("o") # Cuantas veces se repite esa letra
print(count)
print("----------------------------")
cadena3 = resultado.replace("o","x") # Cambia una letra por otra
print(cadena3)
cadena3 = resultado.split(' ') # Separa por palabras la cadena
print(cadena3)
