import tkinter as tk
import logica as lg
from tkinter import messagebox

def button_matricula():
    menu_registro = tk.Toplevel()
    menu_registro.geometry("400x200")
    menu_registro.title("registro")

window = tk.Tk()

window.geometry("400x300")
window.title("login")

name_var = tk.StringVar()
name_frame = tk.Frame(window)
name_frame.pack()
name_label = tk.Label(name_frame, text="Nombre")
name_label.pack()
name_entry = tk.Entry(name_frame, textvariable=name_var)
name_entry.pack()


paterno_var = tk.StringVar()
paterno_frame = tk.Frame(window)
paterno_frame.pack()
paterno_label = tk.Label(paterno_frame, text="Apellido Paterno")
paterno_label.pack()
paterno_entry = tk.Entry(paterno_frame, textvariable=paterno_var)
paterno_entry.pack()

materno_var = tk.StringVar()
materno_frame = tk.Frame(window)
materno_frame.pack()
materno_label = tk.Label(materno_frame, text="Apellido Materno")
materno_label.pack()
materno_entry = tk.Entry(materno_frame, textvariable=materno_var)
materno_entry.pack()


año_var = tk.IntVar()
año_frame = tk.Frame(window)
año_frame.pack()
año_label = tk.Label(año_frame, text="Año de nacimineto")
año_label.pack()
año_entry = tk.Entry(año_frame, textvariable=año_var)
año_entry.pack()

carrera_var = tk.StringVar()
carrera_frame = tk.Frame(window)
carrera_frame.pack()
carrera_label = tk.Label(carrera_frame, text="Carrera")
carrera_label.pack()
carrera_entry = tk.Entry(carrera_frame, textvariable=carrera_var)
carrera_entry.pack()

tk.Button(window, text='generar', command=button_matricula).pack(side=tk.BOTTOM)





window.mainloop()