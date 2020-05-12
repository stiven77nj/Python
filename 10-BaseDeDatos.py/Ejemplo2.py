import sqlite3

conexion = sqlite3.connect("GestionProductos.db")

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE PRODUCTOS
    (
    CODIGO_ARTICULO VARCHAR(50) PRIMARY KEY,
    NOMBRE_ARTICULO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20)
    )
''')

productos = [
    ("AR01","Pelota",20,"Jugueteria"),
    ("AR02","Pantalon",15,"Confeccion"),
    ("AR03","Destornillador",25,"Ferreteria"),
    ("AR04","Jarron",45,"Ceramica")
]

cursor.execute("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

conexion.close()
