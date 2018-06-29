from tkinter import *

def saludar():
	print('Hola!')

def aviso():
	v = Toplevel(ventana)
	mensaje = Label(v,text='AVISO')
	mensaje.pack()

ventana = Tk()
contenedor1 = Frame(ventana)
contenedor1.pack(side=TOP)
boton = Button(contenedor1, text='Apretame',command=saludar)
boton.pack(side=LEFT)
botonSalida = Button(contenedor1, text='Salir',command=ventana.quit)
botonSalida.pack(side=RIGHT)
contenedor2 =Frame(ventana)
contenedor2.pack(side=BOTTOM)
botonAviso = Button(contenedor2,text='Aviso',command=aviso)
botonAviso.pack()
mainloop()