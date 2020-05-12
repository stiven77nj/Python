'''
Condicionales: Nos permiten comnprobar condiciones y hacer que nuestro programa se
comporte de una forma u otra, que ejecute un fragmento de codigo u otro, dependiendo
de esta condicion.

La estructuras de flujos condicional, se definen mediante el uso de tres palabras
claves reservadas, del lenguaje: if(si), elif(sino,si), y else(sino).
'''
x = int(input("Digite un numero: "))
if x < 0:
    x = 0
    print("Negativo cambiado a cero")

'''
Ahora combinado con elif y else:
'''
numero = int(input("\nDigite un numero: "))
if numero > 0:
    print(f"El numero {numero} es positivo")
elif numero == 0: # -> Elif es conocido en otros lenguajes como: (else if)
    print(f"El numero es cero")
else :
    print(f"El numero {numero} es negativo")
'''
Puede haber cero o mas bloques elif, y el bloque else es opcional. La palabra
elif, es una abreviacion de else if. Una secuencia excesiva if..elif..elif..,
sustituye las sentencias swicth o case encontradas en otros lenguajes.
En python no existen los condicionales multiples.
'''
