
import sqlite3

conexion = sqlite3.connect("Basededatos1.db")

cursor = conexion.cursor()

cursor.execute("SELECT * FROM PERSONAS") # Consultamos personas

personas = cursor.fetchall() # Guardamos todos los datos de la Consulta

for persona in personas:
    print(persona)

# Como no añadimos ni quitamos no se hace commit()
#
conexion.close()
