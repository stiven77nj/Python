# SQLite -> Sistema de base de datos relacionales
# Descargamos la base de datos sqlite

import sqlite3

conexion = sqlite3.connect("Basededatos1.db") # Conectamos una base de datos o la crea si no existe

conexion.close()
