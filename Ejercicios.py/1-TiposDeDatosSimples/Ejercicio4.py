'''
Ejercicio 4:
'''
import math # -> Módulo para saber el valor de pi

print("\n")
radio = float(input("Digite el valor del radio: "))

# -> Con math.pi podemos obtener el valor de pi
area = math.pi * radio**2
longitud = 2 * math.pi * radio

# -> Hacemos area:.2f para tener dos decimales
# -> Si queremos tener tres, ponemos area:.3f, y así sucesivamente
print(f"\nEl area de circulo es: {area:.3f} y su longitud es: {longitud:.3f}")
print("\n")
