'''
Listas: -> Son algo parecido a los arreglos o vectores.
        -> Las listas son una estructura de datos muy flexible, es un grupo
           de elementos (números, cadenas, listas, booleanos, etc) que se
           delimitan por [] y sus elementos se separan por comas ','.
        -> Podemos mostrar el ultimo elemento con el indice -1, y asi
           sucecivamente.
        -> Podemos acceder a las listas por medio de los indices.
        -> Podemos agregar, eliminar y modificar elementos.
'''
cuadrados = [1,4,9,16]
print(cuadrados)
'''
Podemos indexar y rebanar las listas
'''
print("Elemento inicial: ",cuadrados[0])
print("Elemento final: ",cuadrados[-1])
print("Lista rebanada: ",cuadrados[0:2])
'''
Las listas tambien soportan operacioes de concatenacion
'''
print("Concatenando listas: ",cuadrados+[36,49,64])
'''
Podemos modificar los datos de una lista, por ejemplo:
'''
cubos = [1,8,27,65,125] # Vemos que (4**3) = 64 y no 65, entonces
cubos[3] = 64 # Modificamos el elememento de la tercera posicion
print("Cubos: ",cubos)
'''
Podemos agregar nuevos elementos al final de la lista con la funcion append()
Por ejemplo: 6**3 = 216
'''
cubos.append(216) # Ingresamos el numero
print("Cubos: ",cubos)
'''
Podemos cambiar la longitud de la lista e incluso vaciarla totalmente
'''
letras = ['a','b','c','d','e','f','g']
print("Letras: ",letras)
letras[2:5] = ['C','D','E'] # Reemplazamos algunos valores
print("letras: ",letras)
letras[2:5] = [] # Las borramos
print("Letras: ",letras)
letras[:] = [] # Borramos la lista
print("Lista: ",letras)
'''
Usamos la funcion len() para saber cuantos caracteres tiene una lista
'''
print("Numero de caracteres: ",len(letras)) # Habiamos vaciado la lista, debe aparecer cero
'''
Podemos anidar listas (Listas que contengan otras listas)
'''
a = ['a','b','c']
n = [1,2,3]
x = [a,n]
print("Lista con sublistas: ",x)
print("Lista inicial: ",x[0]) # Nos imprime la primera sublista
print("Lista inicial: ",x[0][1]) # Nos imprime de la primera sublista, el elemento en la posicion 1
