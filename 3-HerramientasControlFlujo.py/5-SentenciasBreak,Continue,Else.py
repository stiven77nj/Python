'''
La sentencia break termina el lazo for o while mas anidado.
Las sentencia de lazo pueden tener un else que es ejecutado cuando el lazo
termina.
'''
lista = [1,2,3,4,5]
n = int(input("Digite un numero: ")) # Pedimos un numero para buscarlo en la lista
for i in range(len(lista)):
    if(n == lista[i]):
        print("Numero encontrado")
        break # Una vez encontrado el numero, el break hace que nos salgamos del for y se termine el programa
    else:
        print("Numero no encontrado")
'''
La declaracion continue, continua con la siguiente iteracion del ciclo
'''
print("\n")
for i in range(2,10):
    if i % 2 == 0:
        print(f"Encontre un numero par: {i}")
        continue
    print(f"Encontre un numero: {i}")    
