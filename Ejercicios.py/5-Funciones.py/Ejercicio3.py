'''
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar,
y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje
de IVA, deberá aplicar un 21%.
'''
def total(price, iva):
    if iva == 0:
        totalPrice = (price*21)/100 + price
        return totalPrice
    else:
        totalPrice = (price*iva)/100 + price
        return totalPrice

price = float(input("\nEnter the price to pay: "))
iva = int(input("Enter the iva: "))
result = total(price,iva)
print(f"\nThe total price to pay is: {result}")
