num1 = 5
num2 = 2

try:
    division = num1 / num2
except ZeroDivisionError as error:
    print ("Error: ",error)
    print("No es posible dividir por cero")
else:
    print("Division: ",division)
    print("La division funcion correctamente")
finally:
    print("\nPrograma finalizado")
