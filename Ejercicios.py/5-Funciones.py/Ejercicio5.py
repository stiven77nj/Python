'''
Escribir una función que reciba una muestra de números en una lista
y devuelva su media.
'''
def half(*sample): # Pasamos una secuencia de numeros separados por coma
    return sum(sample)/len(sample) # Calculamos la media

print("\nMean: ",half(1,2,3,4,5))
print("Mena: ",half(2.3,5.7,6.8,9.7,12.1,15.6))
