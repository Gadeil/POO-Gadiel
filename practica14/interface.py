import tkinter as tk
import logica as lg
from tkinter import messagebox


def button_consultar():
    datos = lg.Logica().consultar(user_var.get())
    mostrar = tk.Toplevel()
    mostrar.geometry("400x200")
    mostrar.title("consultar")
    titular = tk.Label(mostrar, text="titular: " + datos["titular"])
    titular.pack()
    edad = tk.Label(mostrar, text="edad: " + str(datos["edad"]))
    edad.pack()
    nip = tk.Label(mostrar, text="nip: " + str(datos["nip"]))
    nip.pack()
    saldo = tk.Label(mostrar, text="saldo: " + str(datos["saldo"]))
    saldo.pack()
    cuenta = tk.Label(mostrar, text="cuenta: " + str(datos["cuenta"]))
    cuenta.pack()


def button_depositar():
    monto = tk.DoubleVar()
    depositar = tk.Toplevel()
    depositar.geometry("400x200")
    depositar.title("Depositar")
    monto_label = tk.Label(depositar, text="monto")
    monto_label.pack()
    monto_entry = tk.Entry(depositar, textvariable=monto)
    monto_entry.pack()

    def boton_depositar():
        lg.Logica().depositar(user_var.get(), monto.get())

    tk.Button(depositar, text='Depositar', command=boton_depositar).pack(side=tk.BOTTOM)


def button_retirar():
    monto = tk.DoubleVar()
    retiro = tk.Toplevel()
    retiro.geometry("400x200")
    retiro.title("retirar")
    monto_label = tk.Label(retiro, text="monto")
    monto_label.pack()
    monto_entry = tk.Entry(retiro, textvariable=monto)
    monto_entry.pack()

    def boton_retiro():
        lg.Logica().retira(user_var.get(), monto.get())

    tk.Button(retiro, text='retirar', command=boton_retiro).pack(side=tk.BOTTOM)


def button_depositar_otro():
    monto = tk.DoubleVar()
    user2 = tk.StringVar()
    deposito_otro = tk.Toplevel()
    deposito_otro.geometry("400x200")
    deposito_otro.title("retirar")
    monto_label = tk.Label(deposito_otro, text="usuario")
    monto_label.pack()
    monto_entry = tk.Entry(deposito_otro, textvariable=user2)
    monto_entry.pack()
    monto_label = tk.Label(deposito_otro, text="monto")
    monto_label.pack()
    monto_entry = tk.Entry(deposito_otro, textvariable=monto)
    monto_entry.pack()

    def boton_retiro_otro():
        value = messagebox.askyesno("Deposito", "estas segudo de depostitar: " + str(monto.get()) + " a "+ user2.get())
        if value:
            lg.Logica().depositar_usuario(user_var.get(), user2.get(), monto.get())
        else:
            messagebox.showinfo("deposito", "deposito cancelado")
    tk.Button(deposito_otro, text='depositar', command=boton_retiro_otro).pack(side=tk.BOTTOM)


def button_principal():
    status = lg.Logica().login(user_var.get(), nip_var.get())
    if status:
        menu = tk.Toplevel()
        menu.geometry("400x200")
        menu.title("Ventana secundaria")
        tk.Button(menu, text='consultar', command=button_consultar).pack(side=tk.BOTTOM)
        tk.Button(menu, text='depositor', command=button_depositar).pack(side=tk.BOTTOM)
        tk.Button(menu, text='retirar', command=button_retirar).pack(side=tk.BOTTOM)
        tk.Button(menu, text='depositar a otra cuenta', command=button_depositar_otro).pack(side=tk.BOTTOM)


window = tk.Tk()

window.geometry("400x200")
window.title("login")
# USER:
user_var = tk.StringVar()
user_frame = tk.Frame(window)
user_frame.pack(side=tk.TOP)
user_label = tk.Label(user_frame, text="usuario")
user_label.pack(side=tk.LEFT)
user_entry = tk.Entry(user_frame, textvariable=user_var)
user_entry.pack(side=tk.RIGHT)

# NIP
nip_var = tk.IntVar()
code_frame = tk.Frame(window)
code_frame.pack(side=tk.TOP)
code_label = tk.Label(code_frame, text="NIP")
code_label.pack(side=tk.LEFT)
code_entry = tk.Entry(code_frame, textvariable=nip_var, show="*")
code_entry.pack(side=tk.RIGHT)

tk.Button(window, text='Generate', command=button_principal).pack(side=tk.BOTTOM)

window.mainloop()