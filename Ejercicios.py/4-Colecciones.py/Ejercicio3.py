'''
Pedir una muestra de numeros, separados por coma, guardarlos en una lista y
mostrar por pantalla su media y desviación típica.
'''
from math import sqrt

limit = int(input("\nEnter the size of the list: "))
print("\n")

list = []
sum = 0
for i in range(0,limit):
    number = int(input("Enter a number: "))
    list.insert(i,number)
    sum += number
half = sum/limit

sum = 0
for i in list:
    sum += (i - half)**2
root = sum/(len(list) - 1)

print(f"\nList: {list}")
print(f"The half is: {half}")
print(f"The typical deviation is: {sqrt(root)}")
