'''
Ejercicio 12:
'''
lista1 = [1,2,3,4,5,1,2,3,4,5]
lista2 = [3,4,5,6,7,3,4,5,6,7]

a = set(lista1)
b = set(lista2)

print(a)
print(b)

union = list(a | b)
soloA = list(a - b)
soloB = list(b - a)
interseccion = list(a & b)

print(union)
print(soloA)
print(soloB)
print(interseccion)
