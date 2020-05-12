import sqlite3

conexion = sqlite3.connect("Basededatos1.db")

cursor = conexion.cursor()

listaPersonas = [('Stiven','Duarte',19),('Roman','Montgomery',22)]

cursor.executemany("INSERT INTO PERSONAS VALUES (?,?,?)", listaPersonas)

conexion.commit()

conexion.close()
