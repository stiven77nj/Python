'''
Generadores: Extraen valores de una funcion y se almacenan en objetos iterables.
             (Se pueden recorrer).
             Cada vez que un generador almacena un valor, esta permanece en un
             estado pausando hasta que se solicita el siguiente. Esta caracteristica
             es conocida como 'suspension de estado'.


    Funcion tradicional                     Generador
    def generarNumeros():                   def generarNumeros():
        return numeros                          yield numeros

Son mas eficientes que las funciones tradicionales.
'''
def generaPares(limite):
    num = 1
    while num < limite:
        yield num*2
        num += 1

valor = generaPares(10)
for i in valor:
    print(i, end = ' ')


print("\n")
def generador(*args):
    for valor in args:
        yield valor * 10, True

for valor1, valor2 in generador(1,2,3,4,5,6,7,8,9):
    print(valor1,valor2, end = ' ')
