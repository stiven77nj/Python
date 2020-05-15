'''
Escribir una funcion que reciba un numero entero prositivo y devuelva su factorial.
'''

def factorial(number):
    fact = 1
    if number < 0:
        print("\nThe number must be positive")
    else:
        for i in range(1,number + 1):
            fact *= i
    return fact

number = int(input("\nEnter a number: "))
print("\nThe factorial the number is: ",factorial(number))
