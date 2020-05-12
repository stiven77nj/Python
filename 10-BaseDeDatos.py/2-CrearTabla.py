import sqlite3

conexion = sqlite3.connect("Basededatos1.db") # Abrimos la base de datos ya creada

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PERSONAS (Nombre TEXT, Apellido TEXT, Edad INTEGER)") # Permite ejecutar cualquier sentencia sql

conexion.commit()

conexion.close()
