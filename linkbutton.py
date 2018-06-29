
#########
# Linkbox
#########


from tkinter import *
import webbrowser

ventana= Tk()
def linkCallback():
	#Aqui abrimos un navegador para acceder a la pag dicha
	webbrowser.open_new(r"http://www.google.com")

#fg cambia el color del texto
link= Button(ventana,text="google",command=linkCallback)
link.pack()
ventana.mainloop()