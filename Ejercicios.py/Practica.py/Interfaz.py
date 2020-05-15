from tkinter import *
from tkinter import messagebox
import sqlite3

# --------------------- Funciones ----------------------------------------------
def conexionBase():
    conexion = sqlite3.connect("Usuarios.db")

    cursor = conexion.cursor()

    try:
        cursor.execute('''
            CREATE TABLE USUARIOS
            (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            APELLIDO VARCHAR(50),
            CONTRASEÑA VARCHAR(50),
            DIRECCION VARCHAR(100)
            )
            ''')
        messagebox.showinfo("Base de Datos","Base de Datos creada con exito")
    except:
        messagebox.showwarning("Atención","La Base de Datos ya existe")


def salirAplicacion():
    valor = messagebox.askquestion("Salir","¿Desea salir de la aplicacion?")
    if valor == 'yes':
        raiz.destroy()

def limpiarCampos():
    miNombre.set("")
    miId.set("")
    miApellido.set("")
    miPassword.set("")
    miDireccion.set("")

def crear():
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO USUARIOS VALUES (NULL,'" + miNombre.get() +
    "','" + miApellido.get() +
    "','" + miPassword.get() +
    "','" + miDireccion.get() + "')")

    conexion.commit()

    messagebox.showinfo("Base de Datos","Registro insertado con exito")

def leer():
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM USUARIOS WHERE ID = " + miId.get())

    usuarios = cursor.fetchall()

    for usuario in usuarios:
        miId.set(usuario[0])
        miNombre.set(usuario[1])
        miApellido.set(usuario[2])
        miPassword.set(usuario[3])
        miDireccion.set(usuario[4])

    conexion.commit()

def actualizar():
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("UPDATE USUARIOS SET NOMBRE = '" + miNombre.get() +
    "', APELLIDO = '" + miApellido.get() +
    "', CONTRASEÑA = '" + miPassword.get() +
    "', DIRECCION = '" + miDireccion.get() +
    "' WHERE ID = " + miId.get())

    conexion.commit()

    messagebox.showinfo("Base de Datos","Registro actualizado con exito")

def eliminar():
    conexion = sqlite3.connect("Usuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM USUARIOS WHERE ID = " + miId.get())

    conexion.commit()

    messagebox.showinfo("Base de Datos","Registro borrado con exito")


# ---------------------- Raiz --------------------------------------------------
raiz = Tk()

# ---------------------- Menu --------------------------------------------------
barraMenu = Menu(raiz)
raiz.config(menu = barraMenu, width = 300, height = 300)
raiz.title("Base de Datos")

basededatos = Menu(barraMenu, tearoff = 0)
basededatos.add_command(label = "Conectar", command = conexionBase)
basededatos.add_command(label = "Salir", command = salirAplicacion)

borrar = Menu(barraMenu, tearoff = 0)
borrar.add_command(label = "Borrar campos", command = limpiarCampos)

crud = Menu(barraMenu, tearoff = 0)
crud.add_command(label = "Crear", command = crear)
crud.add_command(label = "Leer", command = leer)
crud.add_command(label = "Actualizar", command = actualizar)
crud.add_command(label = "Borrar", command = eliminar)

ayuda = Menu(barraMenu, tearoff = 0)
ayuda.add_command(label = "Licencia")
ayuda.add_command(label = "Acerca de...")

barraMenu.add_cascade(label = "BBDD", menu = basededatos)
barraMenu.add_cascade(label = "Borrar", menu = borrar)
barraMenu.add_cascade(label = "CRUD", menu = crud)
barraMenu.add_cascade(label = "Ayuda", menu = ayuda)

# ---------------------- Frame -----------------------------------------------
miframe = Frame(raiz)
miframe.pack()

miId = StringVar()
miNombre = StringVar()
miApellido = StringVar()
miPassword = StringVar()
miDireccion = StringVar()

id = Entry(miframe, textvariable = miId)
id.grid(row = 0, column = 1, padx = 10, pady = 10)
idlabel = Label(miframe, text = "Id : ")
idlabel.grid(row = 0, column = 0, sticky = "e", padx = 10, pady = 10)


nombre = Entry(miframe, textvariable = miNombre)
nombre.grid(row = 1, column = 1, padx = 10, pady = 10)
nombrelabel = Label(miframe, text = "Nombre : ")
nombrelabel.grid(row = 1, column = 0, sticky = "e", padx = 10, pady = 10)

apellido = Entry(miframe, textvariable = miApellido)
apellido.grid(row = 2, column = 1, padx = 10, pady = 10)
apellidolabel = Label(miframe, text = "Apellido : ")
apellidolabel.grid(row = 2, column = 0, sticky = "e", padx = 10, pady = 10)

password = Entry(miframe, textvariable = miPassword)
password.grid(row = 3, column = 1, padx = 10, pady = 10)
password.config(show = "*")
passwordlabel = Label(miframe, text = "Contraseña : ")
passwordlabel.grid(row = 3, column = 0, sticky = "e", padx = 10, pady = 10)

direccion = Entry(miframe, textvariable = miDireccion)
direccion.grid(row = 4, column = 1, padx = 10, pady = 10)
direccionlabel = Label(miframe, text = "Dirección : ")
direccionlabel.grid(row = 4, column = 0, sticky = "e", padx = 10, pady = 10)



raiz.mainloop()
