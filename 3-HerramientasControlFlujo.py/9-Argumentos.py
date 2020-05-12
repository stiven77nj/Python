'''
Cuando ponemos un * al argumento, decimos que esa funcion puede recibir n
cantidad de argumentos.
Recibe los argumentos y los convierte en una tupla
'''
def suma(*argumento): # Podemos pasar n cantidad de argumentos
    print(argumento)
    print(type(argumento)) # Podemos saber que tipo de dato es

resultado = suma(10,50,60,5,6,8) # Si no pasamos ningun argumento nos devuelve una tupla vacia
print(resultado)


def sumados(**kwargs): # Le pasamos los parametros y lo regresa como un diccionario
    valor = kwargs.get('valor','No contiene valor')
    print(valor)
    print(kwargs)

resultado = sumados(valor = "Nicolas", x = 2, y =9, z = True)
print(resultado)

'''
* -> n valores -> tuplas
** -> n valores -> diccionario
'''
