from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorDB import controladorDB

controlador = controladorDB()
#3. Función para disparar el botón
def ejecutaInsert():
    controlador.guardarAlumnos(varNombreNew.get(), varCorNew.get(), varConNew.get())
    
    
#Aquí hacemos un def para la selección de datos
def ejecutaSelectU():
    usuario = controlador.consultarAlumnos(varbus.get()) 
    for usu in usuario:
        cadena = "Id: " + str(usu[0])+ "\n" + " Nombre: " + usu[1]+ "\n" + " Correo: " + usu[2]+ "\n" + " Contraseña: " + str(usu[3])
    
    if (usuario):
        print(cadena)
        textEnc.delete("1.0", END)
        textEnc.insert(END, cadena)


    else:
        messagebox.showinfo("Error", "No se encontró el usuario")
        
#CONSULTAR TODOS LOS USUARIOS
def allSelect():
    tabla.delete(*tabla.get_children())
    usuarios = controlador.BuscarTodoslosAlumnos()
    for usu in usuarios:
        cadena = "Id: " + str(usu[0])+ "\n" + " Nombre: " + usu[1]+ "\n" + " Correo: " + usu[2]+ "\n" + " Contraseña: " + str(usu[3])
        print(cadena)
        tabla.insert('',0, values=(usu[0],usu[1], usu[2], usu[3]))






ventana = Tk()
ventana.title("CRUD de usuarios - Práctica 15")
ventana.geometry("1024x400")


panel = ttk.Notebook(ventana) 
panel.pack(fill='both', expand='yes') 

pestana1 = ttk.Frame(panel) #primera pestaña
pestana2 = ttk.Frame(panel) #segunda pestaña
pestana3 = ttk.Frame(panel) #tercera pestaña
pestana4 = ttk.Frame(panel) #cuarta pestaña
pestana5 = ttk.Frame(panel) #quinta pestaña

#Aquí se colocan como tal todas las pestañas

panel.add(pestana1, text='Agregar Alumno') 
panel.add(pestana2, text='Buscar alumno')
panel.add(pestana3, text='Buscar todos los Alumnos')
panel.add(pestana4, text='Actualizar Alumno')
panel.add(pestana5, text='Eliminar Alumno')


#Pestaña 1: Formulario de Alumno
titulos = Label(pestana1, text="Registro de Alumnos", fg = 'blue', font = ("Modern",18)).pack()

varIDNew = tk.IntVar()
lblCor = Label(pestana1, text="ID: ").pack()
txtCor = Entry(pestana1, textvariable=varIDNew)
txtCor.pack()

varNombreNew = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ").pack()
txtNom = Entry(pestana1, textvariable=varNombreNew)
txtNom.pack()

varCorNew = tk.StringVar()
lblCor = Label(pestana1, text="Correo: ").pack()
txtCor = Entry(pestana1, textvariable=varCorNew)
txtCor.pack()

varConNew = tk.StringVar()
lblCon = Label(pestana1, text="Contraseña: ").pack()
txtCon = Entry(pestana1, textvariable=varConNew)
txtCon.pack()

varGrupNew = tk.IntVar()
lblCon = Label(pestana1, text="Grupo: ").pack()
txtCon = Entry(pestana1, textvariable=varGrupNew)
txtCon.pack()

btnGuardar = Button(pestana1, text="Guardar Usuario",command=ejecutaInsert).pack()

#Pestaña 2. Buscar Alumno

titulo2= Label(pestana2, text="Buscar usuarios", fg = 'green', font = ("Modern",18)).pack()

varbus=tk.StringVar()
lblid=Label(pestana2, text="Id: ").pack() 
txtid=Entry(pestana2, textvariable=varbus).pack()
btnBuscar=Button(pestana2, text="Buscar", command=ejecutaSelectU).pack() 

subBus=Label(pestana2, text="Resultado de la busqueda: ", fg='blue', font=("Modern", 18)).pack() 
textEnc = tk.Text(pestana2, width=52, height=10)
textEnc.pack()

#Pestaña 3. Consultar usuarios
titulo3= Label(pestana3, text="Consultar usuarios:", fg = 'red', font = ("Modern",18))
titulo3.pack()

tabla = ttk.Treeview(pestana3, columns=('#1', '#2', '#3', '#4'), show='headings', height=10)
tabla.heading('#1', text='Id')
tabla.heading('#2', text='Nombre')
tabla.heading('#3', text='Correo')
tabla.heading('#4', text='Contraseña')
tabla.pack()

botonconsulta = Button(pestana3, text="Consultar", command=allSelect)
botonconsulta.pack()




ventana.mainloop()