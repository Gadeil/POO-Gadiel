from tkinter import Tk, ttk, Button, messagebox
from tkinter import *
from logica import *

def userWelcome():
    messagebox.showinfo("¡Bienvenido!","Has iniciado sesión correctamente")

def userRejected():
    messagebox.showerror("ERROR","Un parámetro no es válido. Los patámetros no pueden ser vacíos")

validate = False

ventana = Tk()
ventana.configure(background="#907D6F")
ventana.title("Práctica 12 - Login")
ventana.geometry("450x200")

#grid(row=0, column=0)

emailLabel = Label(ventana, text="Correo").grid(row=0, column=0)
email = StringVar()
ttk.emailEntry = Entry(ventana, textvariable=email).grid(row=0, column=1)

passwordLabel = Label(ventana,text="Contraseña").grid(row=1, column=0)  
password = StringVar()
ttk.passwordEntry = Entry(ventana, textvariable=password, show='*').grid(row=1, column=1)

#boton
def mandar():
    if password.get() == "" or email.get() == "":
        messagebox.showinfo("Error","No valido")
    else:
        messagebox.showinfo("Bienvenido","Estas dentro")

log = ttk.Button(ventana, text="Iniciar sesión", command=mandar)
log.grid(row=4, column=3)

ventana.mainloop()