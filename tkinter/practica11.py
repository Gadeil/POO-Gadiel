
from tkinter import Tk,Frame,Button

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

botonAzul= Button(seccion2,text="boton azul",fg="blue")
botonAzul.grid(row=0, column=0)

botonrojo= Button(seccion2,text="boton rojo",fg="red")
botonrojo.grid(row=1, column=0)


botonrojo= Button(seccion3,text="boton rojo",bg="red")
botonrojo.pack()


#main de ejecucion de la ventana 
ventana.mainloop()