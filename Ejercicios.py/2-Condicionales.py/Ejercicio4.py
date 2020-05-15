'''
Ejercicio 8:
'''
letra = input("\nIngrese un caracter: ").lower() # -> Transformar una letra a minuscula
# Nota: Si ponemos letra.lower(), el método nos retorna una copia en minuscula, pero no se hace un cambio a la variable
# Usamos upper() para transformar una letra a mayuscula
#
if (letra == 'a') or (letra == 'e') or (letra == 'i') or (letra == 'o') or (letra == 'u'):
    print(f"\nEl caracter {letra} es una vocal\n")
else:
    print(f"\nEl caracter {letra} no es una vocal\n")
