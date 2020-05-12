import sqlite3

conexion = sqlite3.connect("Basededatos2.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE PRODUCTOS (ID INTEGER, NOMBRE TEXT, PRECIO INTEGER)")
conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES (1,'IMPRESORA',300)")
conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES (2,'RATON',20)")
conexion.commit()

cursor.execute("INSERT INTO PRODUCTOS VALUES (3,'ORDENADOR',600)")
conexion.commit()

cursor.execute("SELECT * FROM PRODUCTOS")
productos = cursor.fetchall()
for producto in productos:
    print(producto)

conexion.close()
