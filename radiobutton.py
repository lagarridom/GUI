from tkinter import *

def mandar():
	print('Se seleccionó:',var.get())


ventana =Tk()
contenedor1 = Frame(ventana)
contenedor1.pack(side=RIGHT)
contenedor2 = Frame(ventana)
contenedor2.pack(side=TOP)
contenedor3 = Frame(ventana)
contenedor3.pack(side=BOTTOM)
boton = Button(contenedor1,text='Mandar',command=mandar)
boton.pack()
texto = Label(contenedor2,text='Check Buttons')
texto.pack()
var = DoubleVar()
cButton1 = Radiobutton(contenedor3,text='Opción 1',variable = var,value = 1.111)
cButton1.pack(side=LEFT)
cButton2 = Radiobutton(contenedor3,text='Opción 2',variable = var,value = 2.222)
cButton2.pack(side=LEFT)
cButton3 = Radiobutton(contenedor3,text='Opción 3',variable = var,value = 3.333)
cButton3.pack(side=LEFT)

mainloop()