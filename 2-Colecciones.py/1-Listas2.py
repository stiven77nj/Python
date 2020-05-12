
lista = ["Lunes","Martes","Miercoles","Jueves","Viernes",40,True] # -> Podemos agregar otro tipo de datos
print(f"\n{lista[1:6]}") # -> Me imprime los elementos desde el primero hasta la posicion indicada
print(len(lista)) # -> Cantidad de elementos en la lista
print("------------------------------------------------------\n")

lista = [1,2,4,5]
lista.append(6) # -> Agrega un elemento al final de la lista
lista.insert(2,3) # -> Agrega un elemento en la posicion que queremos, primero le pasamos el indice y luego el valor
lista.extend([7,8,9]) # -> Agregamos bastantes elementos al final de la lista
lista2 = [10,11,12]
lista3 = lista + lista2 # -> Podemos sumar listas
print(3 in lista3) # -> Podemos saber si algun valor se encuentra en la lista, nos devuelve True o False
print(lista3.index(6)) # -> Podemos saber en que posicion se encuentra un elemento
print(lista.count(2)) # -> Sabemos cuantas veces aparace un elemento en la lista
lista.pop(1) # -> Elimina un elemento de la lista, le debemos pasar el indice del elemento a eliminar
lista.remove(1) # -> Elimina un elemento de la lista, le debemos pasar el elemento que deseamos eliminar
lista.reverse() # -> Le damos la vuelta a la lista
lista.clear() # -> Eliminamos toda la lista
lista3.sort() # -> Ordenamos elementos de forma ascendente
lista3.sort(reverse = True) # -> Ordenamos la lista de forma descendente
