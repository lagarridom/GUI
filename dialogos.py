from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import askopenfilename
from tkinter.colorchooser import askcolor
from tkinter.simpledialog import askfloat

def salir():
	eleccion = askyesno('Confirmando','Realmente quieres salir?')
	if eleccion:
		showwarning('Nel','No se puede compa')


def elegir1():
	showinfo('Info','Ya empieza la ley seca')

def elegir2():
	showerror('Error','Hubo un error')

def elegir3():
	archivo=askopenfilename()
	print('Recibimos:',archivo)
def elegir4():
	color=askcolor()
	print('Recibimos:',color)
def elegir5():
	numero=askfloat('Ingresa','Ingresa tu estatura:')
	print('Recibimos:',numero)

funciones = [elegir1,elegir2,elegir3,elegir4,elegir5]

ventana = Tk()
for funcion in funciones:
	boton = Button(ventana,text='Boton',command=funcion)
	boton.pack()
boton = Button(ventana,text='Salir',command=salir)
boton.pack()
mainloop()










