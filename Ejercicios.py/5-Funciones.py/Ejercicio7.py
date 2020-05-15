'''
Hacer un menu de opciones para convertir dinero colombiano a:
-> Dolares 
-> Dolar canadiense
-> Euro
-> Libras Esterlinas.
'''

def menu():

    print("\n.:Menu:.")
    print("1.Dolar")
    print("2.Dolar Canadiense")
    print("3.Euro")
    print("4.Libra Esterlina")
    global opc
    opc = int(input("Opcion: "))
    global dinero
    dinero = float(input("\nCantidad que desea cambiar: "))

    if opc == 1:
        dolar()
    elif opc == 2:
        dolarCanadiense()
    elif opc == 3:
        euro()
    elif opc == 4:
        libraEsterlina()
    else:
        print("\nOpcion incorecta\n")

    global resp
    resp = input("\nHacer otro cambio [si/no]: ").lower()
    repetir()


def dolar():
    global cambio
    cambio = dinero/4.025
    print(f"\nCambio Realizado a dolaes, Tienes {cambio:.2f}")

def dolarCanadiense():
    global cambio
    cambio = dinero/2.867
    print(f"\nCambio Realizado a dolar canadiense, Tienes {cambio:.2f}")

def euro():
    global cambio
    cambio = dinero/4.373
    print(f"\nCambio Realizado a euros, Tienes {cambio:.2f}")

def libraEsterlina():
    global cambio
    cambio = dinero/4.997
    print(f"\nCambio Realizado a libra esterlina, Tienes {cambio:.2f}")

def repetir():
    while(resp != "no"):
        menu()

menu()
