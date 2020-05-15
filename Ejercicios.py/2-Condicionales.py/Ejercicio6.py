'''
Ejercicio 10:
'''
print("\n")

saldoInicial = 1000

print("\t.:Menu:.")
print("1.Ingresar Dinero")
print("2.Retirar Dinero")
print("3.Mostrar Dinero")
print("4.Salir")
opcion = int(input("Opcion: "))

if opcion == 1:
    extra = float(input("\nCuanto dinero desea ingresar: "))
    saldoInicial += extra
    print(f"\nDinero en la cuenta: {saldoInicial}")
elif opcion == 2:
    retiro = float(input("\nCuanto dinero desea retirar: "))
    if retiro > saldoInicial:
        print("\nCantidad insuficiente")
    else:
        saldoInicial -= retiro
        print("\nDinero retirado")
        print(f"Dinero en cuenta: {saldoInicial}")
elif opcion == 3:
    print(f"\nSaldo: {saldoInicial}")
elif opcion == 4:
    print("\nGarcias por su servicio")
else:
    print("\nError, opcion no valida\n")
