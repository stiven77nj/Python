
import sqlite3

conexion = sqlite3.connect("Basededatos1.db")

cursor = conexion.cursor()

cursor.execute("UPDATE PERSONAS SET Edad = 30 WHERE Nombre = 'Stiven'") # Actualizamos una persona

conexion.commit()

conexion.close()
