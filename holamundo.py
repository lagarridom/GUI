from tkinter import *
ventana = Tk()
# Poner título a ventana
ventana.title("Un Titulo Mamalon")

saludo = Label(ventana,text = 'Hola Mundo')
saludo.pack(fill=BOTH,expand=YES)
# Necesitamos poner esto para que
# la ventana se mantenga activa
ventana.geometry('200x200')
ventana.mainloop()
