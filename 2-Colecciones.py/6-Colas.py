'''
Colas: -> veremos como podemos simular las colas en python de una forma
          sencilla, agregando elementos con el método .append() y sacando
          elementos por el principio de la cola con el método .pop(0)
'''
cola = ["Maria","Nicolas","Juan"]

cola.append("Carla") # -> Agregamos elementos al final de la cola
cola.pop(0) # -> Sacamos elementos al principio de la cola
# Para sacar el primer elemento debemos poner el indice cero

n = cola.pop(0)

print(f"Atendiendo a: {n}")

print(cola)
