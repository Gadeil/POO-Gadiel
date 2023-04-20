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

titulo=Label(pestana1, text="Insertar",fg="black", font=("Modern",18)).pack()

varNom=tk.StringVar()
etqNom=Label(pestana1,text="Nombre: ").pack()
txtNom=Entry(pestana1,textvariable=varNom).pack()

varCor=tk.StringVar()
etqCor=Label(pestana1,text="Correo: ").pack()
txtCor=Entry(pestana1,textvariable=varCor).pack()

varCon=tk.StringVar()
etqCon=Label(pestana1,text="Contraseña: ").pack()
txtCon=Entry(pestana1,textvariable=varCon).pack()

#butGuardar=Button(pestana1,text="Guardar Usuario",command=ejecutaInsert).pack()


#Pestaña 2, es para la consulta de un usuario

titulo2=Label(pestana2, text="Eliminar",fg="black", font=("Modern",18)).pack()

varBus=tk.StringVar()
etqId=Label(pestana2,text="Identificador Usuario: ").pack()
txtId=Entry(pestana2,textvariable=varBus).pack()

#btnBus=Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()

subBus=Label(pestana2,text="Encontrado:",fg="blue",font=("Modern",15)).pack()
txtEnc=tk.Text(pestana2,height=5,width=52).pack()

panel.add(pestana1,text="insertar")
panel.add(pestana2,text="eliminar")




























Ventana.mainloop()