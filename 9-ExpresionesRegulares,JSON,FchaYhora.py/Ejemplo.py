import re

def buscar(palabra,texto):
    resultado = re.search(palabra,texto)
    return resultado

texto = "Esto es una frase de pruebas para hacer busquedas"
palabra = "frase"

resultado = buscar(palabra,texto)

if resultado:
    print("Palabra encontrada")
    inicial = resultado.start() # Buscamos en que posicion empieza
    final = resultado.end() # Buscamos en que posicion termina
    print("Comienza en la posicion: ",inicial," y finaliza en la posicion: ",final)
else:
    print("Palabra no encontrada")
