from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from logica import ControladorBD 


controlador = ControladorBD()
#3. Función para disparar el botón
def ejecutaInsert():
    controlador.guardarJuego(varNombreNew.get(), varAnoNew.get())
    
#ACTUALIZAR JUEGO
def ejecutaActualizacion():
    controlador.actualizarJuego(varID.get(), varNombre.get(), varAno.get())

#Aquí hacemos un def para la selección de datos
def ejecutaSelectU():
    usuario = controlador.consultarJuego(varbus.get()) 
    for usu in usuario:
        cadena = "Id: " + str(usu[0])+ "\n" + " Nombre: " + usu[1]+ "\n" + " año: " + str(usu[2])+ "\n"
    
    if (usuario):
        print(cadena)
        textEnc.delete("1.0", END)
        textEnc.insert(END, cadena)
        
    else:
        messagebox.showinfo("Error", "No se encontró el juego")

#CONSULTAR TODOS LOS JUEGOS
def allSelect():
    tabla.delete(*tabla.get_children())
    usuarios = controlador.consultarTodosJuegos()
    for usu in usuarios:
        cadena = "Id: " + str(usu[0])+ "\n" + " Nombre: " + usu[1]+ "\n" + " año: " +str(usu[2])+ "\n"
        print(cadena)
        tabla.insert('',0, values=(usu[0],usu[1], usu[2]))


#ELIMINAR USUARIO
def ejecutaEliminar():
    controlador.eliminarJuego(varDeleteID.get())


ventana = Tk()
ventana.title("CRUD de video juegos - examen 3")
ventana.geometry("1024x400")


panel = ttk.Notebook(ventana) 
panel.pack(fill='both', expand='yes') 

pestana1 = ttk.Frame(panel) #primera pestaña
pestana2 = ttk.Frame(panel) #segunda pestaña
pestana3 = ttk.Frame(panel) #tercera pestaña
pestana4 = ttk.Frame(panel) #cuarta pestaña
pestana5 = ttk.Frame(panel) #quinta pestaña


#Aquí se colocan como tal todas las pestañas

panel.add(pestana1, text='Insertar video juego') 
panel.add(pestana2, text='Buscar juego')
panel.add(pestana3, text='Consultar juegos')
panel.add(pestana4, text='Actualizar juegos')
panel.add(pestana5, text='Eliminar juego')

#Pestaña 1: Insertar video juegos
titulos = Label(pestana1, text="Insertar video juego", fg = 'blue', font = ("Modern",18)).pack()

varNombreNew = tk.StringVar()
lblNom = Label(pestana1, text="Nombre: ").pack()
txtNom = Entry(pestana1, textvariable=varNombreNew)
txtNom.pack()

varAnoNew = tk.IntVar()
lblAno = Label(pestana1, text="Año: ").pack()
txtAno = Entry(pestana1, textvariable=varAnoNew)
txtAno.pack()

btnGuardar = Button(pestana1, text="Insertar Juego", command=ejecutaInsert).pack()


#Pestaña 2. Buscar juegos

titulo2= Label(pestana2, text="Buscar juegos", fg = 'green', font = ("Modern",18)).pack()

varbus=tk.StringVar()
lblid=Label(pestana2, text="Id: ").pack() 
txtid=Entry(pestana2, textvariable=varbus).pack()
btnBuscar=Button(pestana2, text="Buscar", command=ejecutaSelectU).pack() 

subBus=Label(pestana2, text="Resultado de la busqueda: ", fg='blue', font=("Modern", 18)).pack() 
textEnc = tk.Text(pestana2, width=52, height=10)
textEnc.pack()

#Pestaña 3. Consultar juego
titulo3= Label(pestana3, text="Consultar juego:", fg = 'red', font = ("Modern",18))
titulo3.pack()

tabla = ttk.Treeview(pestana3, columns=('#1', '#2', '#3'), show='headings', height=10)
tabla.heading('#1', text='Id')
tabla.heading('#2', text='Nombre')
tabla.heading('#3', text='Año')
tabla.pack()

botonconsulta = Button(pestana3, text="Consultar juego", command=allSelect)
botonconsulta.pack()


#Pestaña 4. Actualizar Juego
titulo4= Label(pestana4, text="Actualizar juego", fg = 'orange', font = ("Modern",18)).pack()

varID = tk.StringVar()
lblID = Label(pestana4, text="Id: ").pack()
txtID = Entry(pestana4, textvariable=varID).pack()

varNombre = tk.StringVar()
lblNom = Label(pestana4, text="Nombre: ").pack()
txtNom = Entry(pestana4, textvariable=varNombre).pack()

varAno = tk.StringVar()
lblCor = Label(pestana4, text="Año: ").pack()
txtCor = Entry(pestana4, textvariable=varAno).pack()

btnActualizar = Button(pestana4, text="Actualizar juego", command=ejecutaActualizacion).pack()

#Pestaña 5. Eliminar juego
titulo5= Label(pestana5, text="Eliminar juego", fg = 'purple', font = ("Modern",18)).pack()

varDeleteID = tk.StringVar()
lblID = Label(pestana5, text="Id: ").pack()
txtID = Entry(pestana5, textvariable=varDeleteID).pack()

btnEliminar = Button(pestana5, text="Eliminar juego", command=ejecutaEliminar).pack()

ventana.mainloop()