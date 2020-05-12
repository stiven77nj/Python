from tkinter import *

'''
Raiz
'''
raiz = Tk()
raiz.title("Ventana de Pruebas")
# raiz.resizable(0,0) # El primero es el ancho y el otro el alto, con (0,0) No se puede redimensionar
# Podemos tambien usar (1,0), el primero se puede modificar pero el segundo no
raiz.iconbitmap("11-InterfazGrafica.py\ThePunisher.ico") # Cambiar el icono de la barra de la interfaz
# raiz.geometry() # Podemos poner el tamaño que deseamos


'''
Frame
'''
miframe = Frame(raiz, width = 2000, height = 2000)
# miframe.config(bg = "white") # Damos color al frame
# miframe.config(bd = 35)  Cambiamos el grosor del borde
# miframe.config(relief = 'groove') # Cambiamos la forma del borde
# miframe.config(cursor = "hand2") # Cambia la forma del cursor
miframe.pack() # Empaquetamos la raiz con el frame como queramos


minombre = StringVar() # Nombre como cadena de caracteres


'''
Entry
'''
nombreEntry = Entry(miframe, textvariable = minombre)
nombreEntry.grid(row = 0, column = 1, padx = 10, pady = 10) # Creamos filas y columnas

apellidoEntry = Entry(miframe)
apellidoEntry.grid(row = 1, column = 1, padx = 10, pady = 10)

direccionEntry = Entry(miframe)
direccionEntry.grid(row = 2, column = 1, padx = 10, pady = 10)

passwordEntry = Entry(miframe)
passwordEntry.config(show = '*')
passwordEntry.grid(row = 3, column = 1, padx = 10, pady = 10)


'''
Text
'''
comentarioText = Text(miframe, width = 16, height = 5)
comentarioText.grid(row = 4, column = 1, padx = 10 , pady = 10)
scrollvert = Scrollbar(miframe, command = comentarioText.yview) # Creamos el scroll
scrollvert.grid(row = 4, column = 2, sticky = "nsew")
comentarioText.config(yscrollcommand = scrollvert.set)


'''
Label
'''
nombrelabel = Label(miframe, text = "Nombre: ")
nombrelabel.config(fg = "black", font = ('Arial',10))
nombrelabel.grid(row = 0, column = 0, sticky = "w", padx = 10, pady = 10 )

apellidolabel = Label(miframe, text = "Apellido: ")
apellidolabel.config(fg = "black", font = ("Arial",10))
apellidolabel.grid(row = 1, column = 0, sticky = "w", padx = 10, pady = 10)

direccionlabel = Label(miframe, text = "Direccion: ")
direccionlabel.config(fg = "black", font = ("Arial",10))
direccionlabel.grid(row = 2, column = 0, sticky = "w", padx = 10, pady = 10)

passwordlabel = Label(miframe, text = "Contraseña: ")
passwordlabel.config(fg = "black", font = ("Arial",10))
passwordlabel.grid(row = 3, column = 0, sticky = "w", padx = 10, pady = 10)

comentarioslabel = Label(miframe, text = "Comentarios: ")
comentarioslabel.config(fg = "black", font = ("Arial",10))
comentarioslabel.grid(row = 4, column = 0, sticky = "w", padx = 10, pady = 10)


'''
Boton
'''
def codigoBoton():
     minombre.set("Nicolas") # Establecemos el nombre

boton = Button(raiz, text = "Enviar: ", command = codigoBoton)
boton.pack()


raiz.mainloop() # Hacemos que la ventana se mantenga abierta, es como un bucle inifito
