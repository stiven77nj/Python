'''
Pedir al usuario una palabra y luego mostrar en pantalla una a una las letras del
de la palabra introducida empezando por la última.
'''
palabra = input("\nIngrese una palabra: ")

letras = list(palabra)

numeroLetras = len(letras)
print(f"\nNumero de letras de la palabra: {numeroLetras}")

i = -1
print("\nLa palabra escrita al reves es: ")
while i >= (numeroLetras * -1):
    print(letras[i], end ="")
    i -= 1
