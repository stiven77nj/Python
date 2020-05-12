'''
Una variable puede contener valores de diversos tipos. Entre ellos:
'''
'''
Cadena de texto (string):
1). La cadenas de texto las podemos expresar por medio de comillas simples ('..')
    o dobles ("...") con el mismo resultado.
2). Las cadenas de texto pueden ser concatenadas con el operador (+) y repetidas con (*).
3). Las cadenas de texto se pueden indexar(subindices), el primer caracter de la cadena
    tiene el indice 0.
4). Si ponemos indices negativos, empezamos a contar desde la derecha y el primer
    indice es el  numero -1.
5). Podemos usar las rebanadas, que nos permiten obtener subcadenas.
    Los índices de las rebanadas tienen valores por defecto útiles; el valor por
    defecto para el primer índice es cero, el valor por defecto para el segundo índice es
    la longitud de la cadena a rebanar.
'''

print(3*'un'+'ium')
palabra = "Python"
print("Primer caracter: ",palabra[0]) # Primer caracter de la palabra
print("Ultimo caracter: ",palabra[-1]) #Ultimo caracter de la palabra
print("Subcadena: ",palabra[0:3]) # caracteres desde la posicion 0 (incluida) hasta la 3 (excluida)
print("Cadea al reves",palabra[::-1]) # Mosatramos toda la cadena al reves
print("---------------------------")

'''
Numeros:
1). Numero entero.
2). Numero con parte decimal.
3). Numero entero octal.
4). Numero entero hexadecimal.
'''
edad = 15
print("Edad: ",edad)
decimal = 4.5
print("Decimal: ",decimal)
enteroOctal = 043
print("Entero octal: ",enteroOctal)
enteroHexadecimal = 0x23
print("Entero hexadecimal: ",enteroHexadecimal)
print("---------------------------")
'''
Booleanos (verdadero/falso):
'''
verdadero = True
falso = False
print(verdadero)
print(falso)
