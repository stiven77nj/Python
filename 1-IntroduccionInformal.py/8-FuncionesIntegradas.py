'''
Funciones Integradas
'''
# int(): Transforma una cadena a un entero
n = int("10")
print(n)
print("\n")

# float(): Transforma una cadena a un flotante
f = float("10.5")
print(f)
print("\n")

# str(): Transforma cualquier valor a una cadena
c = "Un texto y dos numeros ",str(10)," y ",str(3.14)
print(c)
print("\n")

# bin(): Conversión de entero a binario
n = bin(10)
print(n)
print("\n")

# hex(): Conversión de entero a hexadecimal
n = hex(10)
print(n)
print("\n")

# int(numero,base): Reconversion a entero
print(int("0b1010",2))
print(int("0xa",16))
print("\n")

# abs(): Valor absoluto de un número
print(abs(-10))
print("\n")

# round(): Redondeo de un flotante a entero, menor de .5 a la baja, mayor o igual a .5 al alza
n = round(5.4)
x = round(5.6)
print(n)
print(x)
print("\n")

# len(): Longitud de una colección o cadena
n = len("Python")
print(n)
print("\n")
