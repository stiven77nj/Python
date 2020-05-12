
import sqlite3

conexion = sqlite3.connect("Basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS ORDER BY Edad") # Ordenamos los datos por la edad

lista_ordenada = cursor.fetchall()

for persona in lista_ordenada:
    print(persona)

conexion.close()
