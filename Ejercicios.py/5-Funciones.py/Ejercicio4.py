'''
Escribir una función que calcule el área de un círculo y otra que calcule el
volumen de un cilindro usando la primera función.
'''
import math

def circleArea(radius):
    a = 2 * math.pi * pow(radius,2)
    return a

def circleVolume(radius, height):
    r = circleArea(radius)
    v = r * height
    return v

radius = float(input("\nEnter the radius of the circle: "))
height = float(input("Enter the height of the circle: "))

area = circleArea(radius)
volume = circleVolume(radius, height)
print(f"\nThe area of the circle is: {area:.3f}")
print(f"The volume of the circel is: {volume:.3f}")
