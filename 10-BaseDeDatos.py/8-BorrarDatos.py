
import sqlite3

conexion = sqlite3.connect("Basededatos1.db")

cursor = conexion.cursor()

cursor.execute("DELETE FROM PERSONAS WHERE Nombre = 'Nicolas'") # Borra un elemento con una determinada condicion

conexion.commit()

conexion.close()
