from tkinter import *
from tkinter import ttk
import tkinter as tk

Ventana=Tk()
Ventana.title("CRUD de Usuarios")
Ventana.geometry("500x300")

panel= ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)

titulo=Label(pestana1, text="Insertar",fg="black", font=("Modern",18)).pack()

varNom=tk.StringVar()
etqNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()


#butGuardar=Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()


#Pestaña 2, es para la consulta de un usuario

titulo2=Label(pestana2, text="Eliminar",fg="black", font=("Modern",18)).pack()

varBus=tk.StringVar()
etqId=Label(pestana2,text="Identificador Usuario: ").pack()
txtId=Entry(pestana2,textvariable=varBus).pack()

#btnBus=Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()



titulo3=Label(pestana3, text="consultar",fg="black", font=("Modern",18)).pack()
subBus=Label(pestana3,text=":",fg="blue",font=("Modern",15)).pack()


varBus=tk.StringVar()
etqId=Label(pestana3,text="consultar: ").pack()





panel.add(pestana1,text="insertar")
panel.add(pestana2,text="eliminar")
panel.add(pestana3,text="Consultar ")




























Ventana.mainloop()