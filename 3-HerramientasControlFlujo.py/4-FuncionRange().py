'''
La funcion range() nos permite iterar sobre una secuencia de numeros, debido
a que genera progresiones aritmeticas.
'''
n = 5
for i in range(n):
    print(i, end = ' ')
'''
El valor final dado nunca es parte de la secuencia, por jemplo:
range(10) genera 10 valores = 0,1,2,3,4,5,6,7,8,9.
'''
'''
Es posible hacer que el rango empieze con otro numero, o especificar un
incremento diferente (incluso negativo).
'''
print("\n")
for i in range(5,10): # (Limite inferior , Limite superior)
    print(i, end = ' ')

print("\n")
for i in range(2,10,2): # (Limite inferior, Limite superior, Incremento)
    print(i, end = ' ')
'''
Para iterar sobre los índices de una secuencia, podés combinar range() y len() así:
'''
print("\n")
lista = [1,2,3,4,5,6,7]
for i in range(len(lista)): # Recorremos la lista y le pasamos como parametro el tamaño de la lista
    print(lista[i], end = ' ')

print("\n")
for i in range(len(lista)): # Recorremos la lista y mostramos la posicion y el elemento en dicha posicion
    print(i, " -> ",lista[i])
'''
El objeto devuelto por range() se comporta como si fuera una lista pero no es una lista.
Es un objeto que devuelve los items sucesivos de la secuencia deseada cuando iteras
sobre el, pero no construye una lista, ahorrando espacio en memoria.
'''
'''
Con la funcion list() podemos crear una lista y si la usamos con la funcion range(),
podemos crear una lista a partir de iterables.
'''
print("\n")
numeros = list(range(20)) # Estamos creando una lista
print(numeros)
