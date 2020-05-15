'''
Ejercicio 9:
'''
n1 = float(input("\nNumero 1: "))
n2 = float(input("Numero 2: "))
operacion = input("Digite la operacion: ").upper();

if (operacion == 'S'):
    suma = n1 + n2
    print(f"\nLa suma es: {suma} \n")
elif (operacion == 'R'):
    resta = n1 - n2
    print(f"\nLa resta es: {resta} \n")
elif (operacion == 'M'):
    mult = n1 * n2
    print(f"\nLa multiplicacion es: {mult} \n")
elif (operacion == 'D'):
    div = n1/n2
    print(f"\nLa division es: {div:.2f} \n")
else:
    print("\nCaracter no valido\n")
