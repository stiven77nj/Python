'''
Escribir una función que calcule el máximo común divisor de dos números y otra
que calcule el mínimo común múltiplo.
'''

def mcm(n,m):
    if n > m:
        greater = n
    else:
        greater = m
    while (greater%n != 0) or (greater%m != 0):
        greater +=1
    return greater

def MCD(n,m):
    rest = 0
    while m > 0:
        rest = m
        m = n % m
        n = rest
    return n


n = int(input("\nEnter the number one: "))
m = int(input("Enter the number two: "))

mc = mcm(n,m)
MC = MCD(n,m)

print(f"\nmcm: {mc}")
print(f"MCD: {MC}")
