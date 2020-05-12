from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
raiz = Tk()

def infoAdicional():
    messagebox.showinfo("Procesador de Nicolas","Procesador de textos version 2020")

def avisoLicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")

def salirAplicacion():
    # valor = messagebox.askquestion("Salir","¿Deseas salir de la aplicacion?")
    valor = messagebox.askokcancel("Salir","¿Deseas salir de la aplicacion?")
    if valor == True:
        raiz.destroy()

def cerrarDocumento():
    valor = messagebox.askretrycancel("Reintentar","No es posible cerrar. Documento bloqueado")
    if valor == False:
        raiz.destroy()

def abrirFichero():
    rutaFichero = filedialog.askopenfilename(title = "Abrir", initialdir = "c:")
    print(rutaFichero)

barraMenu = Menu(raiz)
raiz.config(menu = barraMenu, width = 300, height = 300)

archivoMenu = Menu(barraMenu, tearoff = 0)
archivoMenu.add_command(label = "Nuevo")
archivoMenu.add_command(label = "Abrir", command = abrirFichero)
archivoMenu.add_separator()
archivoMenu.add_command(label = "Guardar")
archivoMenu.add_command(label = "Guardar como")
archivoMenu.add_separator()
archivoMenu.add_command(label = "Cerrar", command = cerrarDocumento)
archivoMenu.add_command(label = "Salir", command = salirAplicacion)

archivoEdicion = Menu(barraMenu, tearoff = 0)
archivoEdicion.add_command(label = "Copiar")
archivoEdicion.add_command(label = "Cortar")
archivoEdicion.add_command(label = "Pegar")

archivoHerramientas = Menu(barraMenu, tearoff = 0)

archivoAyuda = Menu(barraMenu, tearoff = 0)
archivoAyuda.add_command(label = "Licencia", command = avisoLicencia)
archivoAyuda.add_command(label = "Acerca de...", command = infoAdicional)

barraMenu.add_cascade(label = "Archivo", menu = archivoMenu)
barraMenu.add_cascade(label = "Edición", menu = archivoEdicion)
barraMenu.add_cascade(label = "Herramientas", menu = archivoHerramientas)
barraMenu.add_cascade(label = "Ayuda", menu = archivoAyuda)

raiz.mainloop()
