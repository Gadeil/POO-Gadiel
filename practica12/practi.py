

from tkinter import Tk,Frame,Button,messagebox,Entry,Label

import logica

# def aviso():
#      if caja1 == "tonogar@gmail.com" and caja2 == "12345":
#           messagebox.showinfo("aviso","bienvenido")
#      else:
#           messagebox.showinfo("aviso","Error")
        
#sp=logica()
ventana = Tk()
ventana.title("Practica 11: Frames")
ventana.geometry("300x150")

seccion1=Frame(ventana,bg="#D19364")
seccion1.pack(expand=True,fill="both")


etiqueta1=Label(seccion1,text="ingresa tu correo",fg="black")
etiqueta1.place(x=5, y=20)

caja1=Entry(seccion1,text="hey",fg="#000")
caja1.place(x=120, y=50)

etiqueta2= Label(seccion1,text="ingresa tu contra",fg="black")
etiqueta2.place(x=5, y=50)

caja2=Entry(seccion1,text="hey",fg="#000")
caja2.place(x=120, y=20)

botoncorreo= Button(seccion1,text="login",fg="black")
botoncorreo.place(x=140, y=100)


ventana.mainloop()