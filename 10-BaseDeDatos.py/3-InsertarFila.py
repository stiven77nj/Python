
import sqlite3

conexion = sqlite3.connect("Basededatos1.db")

cursor = conexion.cursor()

cursor.execute("INSERT INTO PERSONAS VALUES ('Nicolas','Jaimes',19)") # Insertamos una fila

conexion.commit()

conexion.close()
