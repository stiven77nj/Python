'''
Pilas: -> veremos como simular la estructura de datos LIFO pila (stack) y lo
          haremos con ayuda de las listas utilizando sus métodos .append() y .pop()
          para simular la entrada y salida de datos de la pila.
'''

pila = [1,2,3]

pila.append(4) # -> Agregamos elementos al final de la pila
pila.pop() # -> Sacamos elementos al final de la pila
n = pila.pop()
print(f"Sacando el elemento {n}")
print(pila)
