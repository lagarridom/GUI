from tkinter import *

# Extras para tkinter
from tkinter import ttk

def mandar():
	print('Recibí:',combo.get())

ventana = Tk()
combo = ttk.Combobox(ventana)
combo.pack()
combo['values'] = ('Mexico','Corea','Alemania','Suecia')
boton=Button(text='Mandar',command=mandar)
boton.pack()
ventana.mainloop()