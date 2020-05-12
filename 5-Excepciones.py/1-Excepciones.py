'''
Excepciones: Son errores que ocurren durante la ejecucion del programa. La sintaxis
             del codigo es correcta pero durante la ejecucion ha ocurrido algo inesperado.

Dentro del try se coloca lo que se intenta ejecutar.
Dentro de except se coloca lo que se va a ejecutar cuando lo de try falla.
finally se va a ejecutar siempre.
'''

try:
    print(2/0)
except ZeroDivisionError as error: # Se debe colocar el error que marca
    print(error) # Imprimos el error
    print("No es posible dividir por cero")
finally:
    print("Se termino el script")


print("\n")
try:
    lista = [1,2]
    print(lista[9])
except Exception as error: # Si ponemos exception, atrapa cualquier tipo de error
    print(error)
    print("No es posible obtener el valor de la posicion 9")
finally:
    print("Se termino el script")
