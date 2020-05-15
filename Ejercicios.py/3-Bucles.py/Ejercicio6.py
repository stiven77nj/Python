'''
Pedir un numero entero y mostrar por pantalla un triangulo rectangulo de la forma:
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
'''

n = int(input("\nIngrese un numero: "))

for i in range(1, n+1, 2):
    for j in range(i, 0, -2):
        print(j, end = " ")
    print("")
