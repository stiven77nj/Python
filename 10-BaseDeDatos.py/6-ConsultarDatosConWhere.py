
import sqlite3

conexion = sqlite3.connect("Basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS WHERE Edad > 20") # Consultamos perosnas mayores a 20 años

personas_seleccionadas = cursor.fetchall()

for persona in personas_seleccionadas:
    print(persona)

conexion.close()
