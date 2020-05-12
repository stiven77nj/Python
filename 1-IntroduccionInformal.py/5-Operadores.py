'''
Operadores Aritméticos
'''
valor1 = 3
valor2 = 3
resultado = valor1**valor2 * (13/5 - (2*4))

# Usamos el doble ** para potencia

print("El resultado es: ",resultado)
print("\n")



'''
Operadores Relacionales: -> Utilizamos para establecer una relacion entre dos valores.
                         -> Compara estos valores entre si y esta comparacion produce
                            resultado de certeza o falsedad.
                         -> Tienen el mismo nivel de prioridad en su evaluacion.
                         -> Tienen menor prioridad que los operadores aritmeticos.
'''
total = 10 < 20
print("10 es menor que 20: ",total)
total = 10 <= 20
print("10 es menor o igual que 20: ",total)
total = 10 > 20
print("10 es mayor que 20: ",total)
print("\n")



'''
Operadores Logicos: Permiten construir expresions logicas, se obtiene como
                    resultado booleanos.
                    -> and
                    -> or
                    -> not
'''
a = 10
b = 15
c = 20
resultado = ((a<b) and (b<c))
print("((a<b) and (b<c)) = ",resultado)
print("\n")



'''
Prioridad de los operadores en general: 1. ()
                                        2. **
                                        3. *, /, mod, not
                                        4. +, -, and
                                        5. >, <, ==, >=, <=, !=, or
'''
