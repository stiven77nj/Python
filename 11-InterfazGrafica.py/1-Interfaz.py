import tkinter
from tkinter import messagebox
from tkinter import filedialog

# Creamos el componente Raiz
raiz = tkinter.Tk()
raiz.title("Mi programa")
raiz.iconbitmap("11-InterfazGrafica.py\ThePunisher.ico")

# Creamos el componente Frame
miframe = tkinter.Frame(raiz)
miframe.config(bg = 'blue', width = 400, height = 300)
miframe.pack() #

# Creamos el componente label
texto = "Hola mundo"
etiqueta = tkinter.Label(raiz, text = texto)
etiqueta.config(fg = 'black', bg = 'lightgrey', font = ("Roboto", 15))
etiqueta.pack()

# Creamos el componente entry (Texto corto para la entrada de datos)
entrada = tkinter.Entry(raiz)
entrada.config(justify = "center", show = "*") # Mostramos como si fuera password
entrada.pack()

# Creamos el componente text(Texto largo para la entrada de datos)
entrada = tkinter.Text(raiz)
entrada.config(width = 20, height = 10, font = ("Lato", 15), padx = 10, pady = 10, fg = "black", selectbackground = "lightgrey")
entrada.pack()

# Creamos el componente button
def accion():
    print("Hola mundo de nuevo")

boton = tkinter.Button(miframe, text = "Ejecutar", command = accion)
boton.pack()

# Creamos el componente radiobutton
def seleccionar():
    print("Lo opcion seleccionada es: {}".format(opcion.get()))

opcion = tkinter.IntVar()

radiobutton1 = tkinter.Radiobutton(raiz, text = "Opción 1", variable = opcion, value = 1, command = seleccionar)
radiobutton1.pack()

radiobutton2 = tkinter.Radiobutton(raiz, text = "Opción 2", variable = opcion, value = 2, command = seleccionar)
radiobutton2.pack()

radiobutton2 = tkinter.Radiobutton(raiz, text = "Opción 3", variable = opcion, value = 3, command = seleccionar)
radiobutton2.pack()

# Creamos el componente checkbutton
def verificar():
    valor = check1.get()
    if valor == 1:
        print("El check esta activado")
    else:
        print("El check esta desactivado")

check1 = tkinter.IntVar()
boton1 = tkinter.Checkbutton(raiz, text = "Opcion 1", variable = check1, onvalue = 1, offvalue = 0, command = verificar)
boton1.pack()

# Creamos el componente messagebox
def avisar():
     tkinter.messagebox.showinfo("Titulo","Mensaje con la informacion")

boton = tkinter.Button(raiz, text = "Pulsar para aviso", command = avisar)
boton.pack()

# Componente para messagebox para realizar una preguntar
def preguntar():
    resultado = tkinter.messagebox.askquestion("Titulo de la pregunta", "¿Quieres borrar este mensaje?")
    if resultado == 'yes':
        print("Si quiero borrar el archivo")
    else:
        print("No quiero borrar el archivo")

boton = tkinter.Button(raiz, text = "Pulsar para preguntar", command = preguntar)
boton.pack()

# Componente fidelog para abrir un fichero
def abrirFichero():
    rutaFichero = filedialog.askopenfilename(title = "Abrir un fichero")
    print(rutaFichero)

boton = tkinter.Button(raiz, text = "Pulsar para empezar", command = abrirFichero)
boton.pack()


raiz.mainloop()
