from tkinter import *

def mandar():
	print('Recibí:',spin.get())

ventana = Tk()
spin = Spinbox(ventana,from_=0,to=10)
spin.pack()
boton = Button(text='Mandar',command=mandar)
boton.pack()
mainloop()