'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
Si el divisor es cero el programa debe mostrar un error.
'''

n1 = float(input("\nNumero uno: "))
n2 = float(input("Numero dos: "))

if n2 != 0:
    division = n1 / n2
    print(f"\nLa division es: {division}")
else:
    print("\nNo se puede divir por cero")
