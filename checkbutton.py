from tkinter import *

def mandar():
	print('Opción1:',var1.get())
	print('Opción2:',var2.get())
	print('Opción3:',var3.get())


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
var1 = IntVar()
cButton1 = Checkbutton(contenedor3,text='Opción 1',variable = var1)
cButton1.pack(side=LEFT)
var2 = IntVar()
cButton2 = Checkbutton(contenedor3,text='Opción 2',variable = var2)
cButton2.pack(side=LEFT)
var3 = IntVar()
cButton3 = Checkbutton(contenedor3,text='Opción 3',variable = var3)
cButton3.pack(side=LEFT)

mainloop()