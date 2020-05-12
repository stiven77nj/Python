from tkinter import *

raiz = Tk()

opcion = IntVar()

def imprimir():
    # print(opcion.get())
    if opcion.get() == 1:
        etiqueta.config(text = "Genero masculino")
    else:
        etiqueta.config(text = "Genero femenino")

milabel = Label(raiz, text = "Genero: ")
milabel.pack()

radioBoton1 = Radiobutton(raiz, text = "Masculino", variable = opcion, value = 1, command = imprimir)
radioBoton1.pack()

radioBoton2 = Radiobutton(raiz, text = "Femenino", variable = opcion, value = 2, command = imprimir)
radioBoton2.pack()

etiqueta = Label(raiz)
etiqueta.pack()

raiz.mainloop()
