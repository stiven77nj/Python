'''
Generadores: -> Nueva instruccion yield from.

Usando yield from simplifica el codigo de los generadores en el caso de utilizar
bucles anidados.
'''
def devuelve_ciudades(*ciudades):
    for elemento in ciudades:
        yield from elemento # Es lo mismo que tener el for anidado: for subelemento in elemento:


ciudades_devueltas = devuelve_ciudades("Madrid","Barcelona","Bilbao","Valencia")
print(next(ciudades_devueltas), end = '')
print(next(ciudades_devueltas))
