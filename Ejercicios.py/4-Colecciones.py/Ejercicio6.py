'''
Escibir un programa que guarde en un diccionario los precios de las frutas.
Preguntar al usuario por una fruta, un peso en kilos y mostrar por pantalla
el precio de ese numero de Kilos de fruta. Si la fruta no esta se debe mostrar
un mensaje con el error.

Fruta    Precio
Platano 1.35
Manzana  0.80
Pera     0.85
Naranja  0.70
'''
fruits = {"Banana":1.35, "Apple":0.80, "Pear":0.85, "Orange":0.70}

fruit = input("\nEnter the name of the fruit: ").title()
kilograms = float(input("Enter the number of kilograms: "))

if fruit in fruits:
    price = kilograms * fruits[fruit]
    print(f"\nThe price to pay is: {price:.2f}")
else:
    print("\nThe fruit isn't in the dictionary")
