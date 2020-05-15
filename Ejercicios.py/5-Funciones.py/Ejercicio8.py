'''
Realizar un programa para evaluar los conociminetos basicos en operaciones
aritmeticas. Los numeros a operar seran dos y seran ingresados por el usuario.
Debera preguntar por el resultado de la suma, resta , multiplicacion y division.
Al final debera mostrar los aciertos y los errores.
'''
def sumar(num1,num2):
    global respUsuario
    global respReal

    respUsuario = float(input(f"\nCuanto suma {num1} + {num2}: "))
    respReal = num1 + num2

    if respUsuario == respReal:
        print("Resultado correcto\n")
        global aciertos
        aciertos += 1
    else:
        print("Resultado erroneo\n")
        global errores
        errores += 1
    print(f"Respuesta usuario: {respUsuario}")
    print(f"Respuesta real: {respReal}")

def restar(num1,num2):
    global respUsuario
    global respReal

    respUsuario = float(input(f"\nCuanto es la resta de {num1} - {num2}: "))
    respReal = num1 - num2

    if respUsuario == respReal:
        print("Resultado correcto\n")
        global aciertos
        aciertos += 1
    else:
        print("Resultado erroneo\n")
        global errores
        errores += 1
    print(f"Respuesta usuario: {respUsuario}")
    print(f"Respuesta real: {respReal}")

def multiplicar(num1,num2):
    global aciertos
    global errores
    global respUsuario
    global respReal

    respUsuario = float(input(f"\nCuanto es la multiplicacion de {num1} * {num2}: "))
    respReal = num1 * num2

    if respUsuario == respReal:
        print("Resultado correcto\n")
        global aciertos
        aciertos += 1
    else:
        print("Resultado erroneo\n")
        global errores
        errores += 1
    print(f"Respuesta usuario: {respUsuario}")
    print(f"Respuesta real: {respReal}")

def dividir(num1,num2):
    global respUsuario
    global respReal

    respUsuario = float(input(f"\nCuanto es la division de {num1} / {num2}: "))
    respReal = num1 / num2

    if respUsuario == respReal:
        print("Resultado correcto\n")
        global aciertos
        aciertos += 1
    else:
        print("Resultado erroneo\n")
        global errores
        errores += 1
    print(f"Respuesta usuario: {respUsuario}")
    print(f"Respuesta real: {respReal}")

aciertos = 0
errores = 0
global resp
resp = "si"

while(resp != "no"):
    global num1
    global num2

    num1 = float(input("\nNumero 1: "))
    num2 = float(input("Numero 2: "))

    sumar(num1,num2)
    restar(num1,num2)
    multiplicar(num1,num2)
    dividir(num1,num2)

    resp = input("\nDesea seguir participando: ").lower()

print(f"\nAciertos: {aciertos}")
print(f"Errores: {errores}\n")
