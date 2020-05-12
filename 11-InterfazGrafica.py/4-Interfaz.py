from tkinter import *

root = Tk()

root.title("Ejemplo")

Playa = IntVar()
Montania = IntVar()
Nieve = IntVar()

def opcionesViaje():
    opcionEscogida = ""
    if Playa.get() == 1:
        opcionEscogida += " Playa"
    if Montania.get() == 1:
        opcionEscogida += " Montaña"
    if Nieve.get() == 1:
        opcionEscogida += " Nieve"
    textoFinal.config(text = opcionEscogida)

miframe = Frame(root)
miframe.pack()

milabel = Label(miframe, text = "Elige destinos", width = 50)
milabel.pack()

checkbutton1 = Checkbutton(miframe, text = "Playa", variable = Playa, onvalue = 1, offvalue = 0, command = opcionesViaje)
checkbutton1.pack()

checkbutton2 = Checkbutton(miframe, text = "Montaña", variable = Montania, onvalue = 1, offvalue = 0, command = opcionesViaje)
checkbutton2.pack()

checkbutton3 = Checkbutton(miframe, text = "Nieve", variable = Nieve,  onvalue = 1, offvalue = 0, command = opcionesViaje)
checkbutton3.pack()

textoFinal = Label(miframe)
textoFinal.pack()

root.mainloop()
