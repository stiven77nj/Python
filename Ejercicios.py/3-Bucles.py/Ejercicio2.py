'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra,
y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

frase = input("\nIngrese una frase: ")
letra = input("Ingrese una letra: ")
contador = 0

for i in frase:
    if letra == i:
        contador += 1

print(f"\nLa letra {letra} aparece en la frase {contador} veces")
