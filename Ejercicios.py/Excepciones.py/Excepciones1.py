
def operacion(num1,num2,num3):
    try:
        resultado = num1 / (num2 - num3)
        return resultado
    except ZeroDivisionError as error:
        return print("No es posible dividir por cero")

operar = operacion(6,3,3)
print("Resultado: ",operar)
