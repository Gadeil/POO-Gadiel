from tkinter import *
from tkinter import ttk
import tkinter as tk
import logica

def romanosTrans():
    logica.logic().roman2int(varNombreNew.get())
    
def arabigosTrans():
    logica.logic().intToRoman(varNombreNew2.get())

ventana = Tk()
ventana.title("CRUD de video juegos - examen 3")
ventana.geometry("1024x400")


panel = ttk.Notebook(ventana) 
panel.pack(fill='both', expand='yes') 

pestana1 = ttk.Frame(panel) #primera pestaña
pestana2 = ttk.Frame(panel) #segunda pestaña


#Aquí se colocan como tal todas las pestañas

panel.add(pestana1, text='conversiones') 


#Pestaña 1: Insertar video juegos
titulos = Label(pestana1, text="ROMANOS", fg = 'blue', font = ("Modern",18)).pack()

varNombreNew = tk.StringVar()
lblNom = Label(pestana1, text="ROMANO: ").pack()
txtNom = Entry(pestana1, textvariable=varNombreNew)
txtNom.pack()

btnGuardar = Button(pestana1, text="TRANSFORMAR", command=romanosTrans).pack()

#Pestaña 1: Insertar video juegos
titulos = Label(pestana2, text="ARABIGOS", fg = 'blue', font = ("Modern",18)).pack()

varNombreNew2 = tk.IntVar()
lblNom2 = Label(pestana1, text="ARABIGOS: ").pack()
txtNom2 = Entry(pestana1, textvariable=varNombreNew2)
txtNom2.pack()

btnGuardar2 = Button(pestana1, text="TRANSFORMAR", command=arabigosTrans).pack()
 

ventana.mainloop()