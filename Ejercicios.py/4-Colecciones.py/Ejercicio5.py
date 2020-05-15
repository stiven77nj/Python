'''
Almacenar los vectores (1,2,3) y (-1,0,2) en dos listas y mostrar por pantalla
su producto punto
'''

list1 = [1,2,3]
list2 = [-1,0,2]

product = 0
for i in range(len(list1)):
    product += list1[i] * list2[i]

print(f"\nThe product point is: {product}")
