
from tkinter import Tk,Frame,Button,messagebox

#4 Funcion de mensajes 
def mostrarMensaje():
    messagebox.showinfo("aviso","esta mensaje es para informar algo")
    messagebox.showerror("error","nada puede malir sal")
    messagebox.askokcancel("pregunta:","ella jugo conmigo")
    print(messagebox.askyesnocancel("pregunta:","ELLA jugo conmigo"))
    
#5 Funcion para agregar botones

def agregarBoton():
    botonrojo.config(text = "+", bg = "green", fg = "white")
    botonNuevo = Button(seccion3,text = "boton nuevo")
    botonNuevo.pack()
    
    

#1 crear ventana
ventana = Tk()
ventana.title("Practica 11: Frames")
ventana.geometry("600x400")

#2. Definir las secciones de la ventana 
seccion1=Frame(ventana,bg="#F00019")
seccion1.pack(expand=True,fill="both")

seccion2=Frame(ventana,bg="#2329FA")
seccion2.pack(expand=True,fill="both")

seccion3=Frame(ventana,bg="#F00019")
seccion3.pack(expand=True,fill="both")

#3. botones 
botonRojo= Button(seccion1,text="boton rojo",fg="red")
botonRojo.place(x=80, y=80)

botonAzul= Button(seccion2,text="boton azul",fg="blue",command=mostrarMensaje)
botonAzul.grid(row=0, column=0)

botonrojo= Button(seccion2,text="boton rojo",fg="red")
botonrojo.grid(row=1, column=0)

#boton  
botonrojov= Button(seccion3,text="boton rojo",bg="red",command= agregarBoton)
botonrojov.pack()


#main de ejecucion de la ventana 
ventana.mainloop()