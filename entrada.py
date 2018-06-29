from tkinter import *

def mandar():
	texto = var.get()
	print('Recibimos',texto)

ventana = Tk()
contenedor1 = Frame(ventana)
contenedor1.pack(side=TOP)
l = Label(contenedor1,text='Ingresa algo: ')
l.pack(side=LEFT)
var = StringVar()
entrada = Entry(contenedor1,textvariable=var)
entrada.pack(side=RIGHT)
contenedor2 = Frame(ventana)
contenedor2.pack(side=BOTTOM)
boton = Button(ventana,text='Mandar',command=mandar)
boton.pack()
mainloop()