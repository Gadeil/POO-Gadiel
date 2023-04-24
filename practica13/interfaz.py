from tkinter import Tk, Button
from tkinter import *
#from interfaz import *
from logica import passwords

passw = passwords() 

def setPassword():
    passw.createPass(length.get(),mayus.get(),special.get())
   


#Ventana de TKinter
window = Tk()
window.configure(background='#52504F') 
window.title("Práctica 13 - Generador de Contraseñas") 
window.geometry("580x380")
length = IntVar() 
lenLabel = Label(window, background='#52504F', text="¿Cuántos caracteres necesitas?").pack()
lenEntry = Entry(window, textvariable=length).pack()


mayus = BooleanVar() 
special = BooleanVar() 
mayusBox = Checkbutton(window, background='#52504F', text='Usar Mayúsculas',variable=mayus, onvalue=True, offvalue=False)
mayusBox.pack() 
specialBox = Checkbutton(window, background='#52504F', text='Caracteres Especial',variable=special, onvalue=True, offvalue=False)
specialBox.pack()

genButton = Button(window, text='Generar Contraseña', command=setPassword).pack()

pLabel = Label(window, background='#52504F', text="Contraseña para copypastear:").pack()


window.mainloop()