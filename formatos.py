from tkinter import *

ventana =Tk()
ventana.title('Tamaños,colores y fuentes')

Label(ventana,text='Rojo en fuente Times',
				fg='red', #Color de letra
				font='Times',#Timop de letra
				bg='black'#Color de fondo
				).pack()

Label(ventana,text='Verde en fuente Helvetica en negritas',
				bg='dark green',
				fg='light green',
				font='Helvetica 16 bold').pack()
Label(ventana,text='Azul en fuente Verdana en cursivas',
				fg='blue',
				bg='yellow',
				font='Verdana 10 italic').pack()

mainloop()