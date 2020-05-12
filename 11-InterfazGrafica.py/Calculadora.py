from tkinter import *
from math import *
import parser

# ----------------- Raiz ------------------------------------------------
raiz = Tk()
raiz.title("Calculadora de Nicolas")
raiz.config(bg = "gray20")
raiz.geometry("400x600")
raiz.resizable(False,False)

# ----------------- Frame -----------------------------------------------
miframe = Frame(raiz)
miframe.config(bg = "gray20")
miframe.pack()

# ----------------- Entry -----------------------------------------------
textoPantalla = StringVar()
pantallaEntry = Entry(miframe, textvariable = textoPantalla)
pantallaEntry.config(bg = "black", fg = "white", justify = "right", font = ("Roboto",20,"italic"), width = 22, borderwidth = 10)
pantallaEntry.grid(row = 1, column = 1, padx = 20, pady = 20, columnspan = 4) # columnspan hace que ocupe mas columnas

# ----------------- Pulsaciones del teclado -----------------------------
operacion = ""
i = 0

def obtenerNumero(n):
    global i
    pantallaEntry.insert(i, n)
    i += 1

def obtenerOperacion(operador):
    global i
    longitudOperador = len(operador)
    pantallaEntry.insert(i, operador)
    i += longitudOperador

def clear():
    pantallaEntry.delete(0, END)

def undo():
    estadoPantalla = pantallaEntry.get()
    if len(estadoPantalla):
        estadoNuevoPantalla = estadoPantalla[:-1]
        clear()
        pantallaEntry.insert(0, estadoNuevoPantalla)
    else:
        clear()
        pantallaEntry.insert(0, "ERROR")

def resultado():
    estadoPantalla = pantallaEntry.get()
    try:
        expresion = parser.expr(estadoPantalla).compile()
        result = eval(expresion)
        clear()
        pantallaEntry.insert(0, result)
    except:
        clear()
        pantallaEntry.insert(0, "ERROR")

# ----------------- Fila de botones 1 -----------------------------------
botonRaiz = Button(miframe, text = "√", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("sqrt"))
botonRaiz.grid(row = 2, column = 1, pady = 10)
botonExp = Button(miframe, text = "Exp", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("**"))
botonExp.grid(row = 2, column = 2, pady = 10)
botonUndo = Button(miframe, text = "←", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : undo())
botonUndo.grid(row = 2, column = 3, pady = 10)
botonClear = Button(miframe, text = "C", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : clear())
botonClear.grid(row = 2, column = 4, pady = 10)

# ----------------- Fila de botones 2 -----------------------------------
botonPareIzq = Button(miframe, text = "(", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("()"))
botonPareIzq.grid(row = 3, column = 1, pady = 10)
botonPareDer = Button(miframe, text = ")", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion(")"))
botonPareDer.grid(row = 3, column = 2, pady = 10)
botonLN = Button(miframe, text = "Ln", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("log"))
botonLN.grid(row = 3, column = 3, pady = 10)
botonDiv = Button(miframe, text = "÷", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("/"))
botonDiv.grid(row = 3, column = 4, pady = 10)

# ----------------- Fila de botones 3 -----------------------------------
boton7 = Button(miframe, text = 7, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(7))
boton7.grid(row = 4, column = 1, pady = 10)
boton8 = Button(miframe, text = 8, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(8))
boton8.grid(row = 4, column = 2, pady = 10)
boton9 = Button(miframe, text = 9, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(9))
boton9.grid(row = 4, column = 3, pady = 10)
botonMult = Button(miframe, text = "x", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("*"))
botonMult.grid(row = 4, column = 4, pady = 10)


# ------------------ Fila de botones 4 -----------------------------------
boton4 = Button(miframe, text = 4, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(4))
boton4.grid(row = 5, column = 1, pady = 10)
boton5 = Button(miframe, text = 5, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(5))
boton5.grid(row = 5, column = 2, pady = 10)
boton6 = Button(miframe, text = 6, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(6))
boton6.grid(row = 5, column = 3, pady = 10)
botonRest = Button(miframe, text = "-", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("-"))
botonRest.grid(row = 5, column = 4, pady = 10)


# ------------------ Fila de botones 5 -----------------------------------
boton1 = Button(miframe, text = 1, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(1))
boton1.grid(row = 6, column = 1, pady = 10)
boton2 = Button(miframe, text = 2, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(2))
boton2.grid(row = 6, column = 2, pady = 10)
boton3 = Button(miframe, text = 3, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(3))
boton3.grid(row = 6, column = 3, pady = 10)
botonSum = Button(miframe, text = "+", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("+"))
botonSum.grid(row = 6, column = 4, pady = 10)


# ------------------ Fila de botones 6 -----------------------------------
botonComa = Button(miframe, text = ",", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("."))
botonComa.grid(row = 7, column = 1, pady = 10)
boton0 = Button(miframe, text = 0, width = 10, height = 3, bg = "black", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerNumero(0))
boton0.grid(row = 7, column = 2, pady = 10)
botonPi = Button(miframe, text = "π", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : obtenerOperacion("pi"))
botonPi.grid(row = 7, column = 3, pady = 10)
botonigual = Button(miframe, text = "=", width = 10, height = 3, bg = "gray14", fg = "white", font = ("Roboto",10,"bold"), command = lambda : resultado())
botonigual.grid(row = 7, column = 4, pady = 10)


raiz.mainloop()
