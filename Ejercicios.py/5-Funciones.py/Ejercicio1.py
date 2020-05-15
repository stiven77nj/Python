'''
Escribir una funcion que reciba una cadena <nombre> y muestre por pantalla el
saludo hola<nombre>
'''
def usuario(name):
    print(f"\nHello {name}")

name = input("\nEnter your name: ").title()
usuario(name)
