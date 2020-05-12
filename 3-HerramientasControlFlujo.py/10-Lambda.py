'''
Lambda nos sirve para crear funciones anonimas en una sola linea de codigo.

     nombre_funcion = Lambda numero_de_argumentos : accion_a_ejecutar
'''
mi_funcion = lambda n1,n2 : n1 + n2

resultado = mi_funcion(10,20)
print(resultado)


formato = lambda sentencia : '{}?'.format(sentencia)

resultado = formato("Puedes hacer esto una pregunta")
print(resultado)


no_valor = lambda : 10
resultado = no_valor()
print(resultado)
