'''
lista = []
for valor in range(0,100):
    lista.append(valor)
print(lista)
'''

# List Comprehension:
# 1). Valor a agregar a lista
# 2). Ciclo
lista = [valor for valor in range(0,101) if valor % 2 == 0 ]
print(lista)

tupla = tuple((valor for valor in range(0,101) if valor % 2 != 0))
print("\n")
print(tupla)

diccionario = {indice:valor for indice,valor in enumerate(lista)}
print("\n")
print(diccionario)
