'''
Ejercicio 6:
'''

n1 = int(input("\nPrimer numero: "))
n2 = int(input("Segundo numero: "))

if (n1%2 == 0) and (n2%2 == 0):
    print("\nLos dos numeros son pares\n")
elif (n1%2 == 0) and (n2%2 != 0):
    print(f"\nEl numero {n1} es par\n")
elif (n1%2 != 0) and (n2%2 == 0):
    print(f"\nEl numero {n2} es par\n")
else:
    print("\nNinguno de los dos numero son pares\n")
