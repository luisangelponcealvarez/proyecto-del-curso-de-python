from tkinter import *

def mensaje():
  print("mensaje del boton")

ventana = Tk()
ventana.title("hola")
ventana.geometry("500x500")

lbl = Label(ventana,text="este es un [label] tkinter")
lbl.pack()

btn = Button(ventana,text="presiona este [button] para mensaje", command=mensaje)
btn .pack()

ventana.mainloop()
