'''
Escribir una función que aplique un descuento a un precio y otra que aplique el
IVA a un precio. Escribir una tercera función que reciba un diccionario con los
precios y porcentajes de una cesta de la compra, y una de las funciones anteriores,
y utilice la función pasada para aplicar los descuentos o el IVA a los productos
de la cesta y devolver el precio final de la cesta.
'''

def applyIva(price,iva = 19): # Funcion oara aplicar el iva a la compra total
    return (price*iva)/100 + price

def applyDiscount(price,discount): # Funcion para aplicar los descuentos a cada producto
    return price - (price*discount)/100

def price_basket(basket): # Funcion con los precios y los descuentos
    total = 0
    for price,discount in basket.items():
        total += applyDiscount(price,discount) # Llamamos la funcion de aplicar los descuentos
    return total

priceNotIva = price_basket({1000:20, 500:10, 100:1})
priceIva = applyIva(priceNotIva)
print(f"\nThe price of the purchase with the discounts is: {priceNotIva}")
print(f"The price of the purchase total with IVA is: {priceIva}")
