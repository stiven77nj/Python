'''
Conjuntos:  -> Son un tipo de colección donde los elementos se agregan
               de forma desordenada y no pueden haber valores duplicados.
            -> Dentro de los conjuntos no pueden haber otro ripo de colecciónes
'''
conjunto = set() # -> Creamos un conjunto vacio
conjunto = {1,2,3,4} # -> Llenamos el conjunto
conjunto.add(9) # -> Agregamos valores al conjunto y lo pone donde quiera
conjunto.add(5.4)
conjunto.discard(4) # -> Eliminamos un elemento del conjunto
# Podemos usar el metodo clear() y eleminamos el conjunto
print(conjunto)

# Creamos el conjunto a y b
a = {1,2,3}
b = {3,4,5}
print(a == b) # -> Miramos si los conjuntos son iguales

c = a | b # -> Union
print(c)

c = a & b # -> Interseccion
print(c)

c = a - b # -> Diferencia
print(c)

c = a ^ b # -> Diferencia simetrica: elementos de a y b, pero no estan en los dos
print(c)

c = {1,2,3,4,5}

print(a.issubset(c)) # -> Saber si a es un subconjunto de C

print(c.issuperset(a)) # -> Saber si C es el super conjunto del conjunto a

print(a.isdisjoint(b)) # -> Saber si los conjunto son disconexos (elementos en comun)

c = forzenset({1,2,3,4,5}), # hacemos que el conjunto sea inmutable
