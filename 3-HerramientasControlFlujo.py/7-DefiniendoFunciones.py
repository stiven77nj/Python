
'''
La plabra reservada 'def' se ultiliza para definir funciones. Despues va el nombre
de la funcion y la lista de parametros formales entre paraentesis. La sentencias
que forman el cuerpo de la funcion empiezan en la lines siguiente y deben estar
con sangria.

def nombreFuncion( parametros ):
    instrucciones
    return -> si se desea

La sentencia return devuelve un valor en una funcion. EL return sin una expresion
como argumento retorna 'None'.
'''
def sumar(n1,n2): # Pasamos parametros
    suma = n1 + n2
    return suma # Retornamos el valor de la suma

n1 = int(input("Numero 1: "))
n2 = int(input("Numero 2: "))
print("La suma es: ",sumar(n1,n2)) # Mostramos el resultado

'''
Podemos crear una funcion que escriba la serie fibonacci hasta un limite determinado
'''
def fibonacci(n): # Pasmos el numero que queremos
    a,b = 0,1
    print("Serie fibonacci: ",end = ' ')
    while(a < n):
        print(a, end = ' ')
        a,b = b,a+b
    print()

n = int(input("\nIngrese un numero: "))
fibonacci(n) # Llamamos a la funcion que acabamos de definir
'''
Mismo ejercicio de la sucesion fibonacci pero retornando una lista:
'''
def fibonacci(n):
    resultado = []
    a,b = 0,1
    while a < n:
        resultado.append(a) # Añadimos el valor de 'a' al final de la lista
        a,b = b,a+b
    return resultado

n = int(input("\nIngrese un numero: "))
print(f"La sucesion fibinacci es: {fibonacci(n)}")

'''
Podemos pasar una funcion como parametro
'''
def multiplicacion(n1,n2):
    return n1*n2

def mostrarResultado(funcion):
    print(funcion(6,8))

mult = multiplicacion
mostrarResultado(mult)
