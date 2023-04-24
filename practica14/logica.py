from tkinter import messagebox
import json


class Logica:
    def __init__(self):
        with open('C://Users//tonog//Documents//GitHub//POO//practica14//usuarios.json') as file:
            self._user_dictionary = json.load(file)

    def login(self, user, nip):
        try:
            if self._user_dictionary[user]["titular"] == user and self._user_dictionary[user]["nip"] == nip:
                messagebox.showinfo("ok", "welcome")
                return True
            else:
                messagebox.showerror("ERROR", "credenciales no validas")
                return False
        except KeyError:
            messagebox.showerror("ERROR", "Usuario no registrado")

    def consultar(self, user):
        return self._user_dictionary[user]

    def depositar(self, user, monto):
        self._user_dictionary[user]["saldo"] = self._user_dictionary[user]["saldo"] + monto
        with open("C://Users//tonog//Documents//GitHub//POO//practica14//usuarios.json", "w") as file:
            json.dump(self._user_dictionary, file)
        messagebox.showinfo("deposito exitoso", "tu nuevo saldo es: " + str(self._user_dictionary[user]["saldo"]))

    def retira(self, user, monto):
        self._user_dictionary[user]["saldo"] = self._user_dictionary[user]["saldo"] - monto
        with open("C://Users//tonog//Documents//GitHub//POO//practica14//usuarios.json", "w") as file:
            json.dump(self._user_dictionary, file)
        messagebox.showinfo("retiro exitoso", "tu nuevo saldo es: " + str(self._user_dictionary[user]["saldo"]))

    def depositar_usuario(self, user, user2, monto):
        try:
            if self._user_dictionary[user]["saldo"] < monto:
                messagebox.showwarning("warning", "saldo insuficiente")
            else:
                self._user_dictionary[user]["saldo"] = self._user_dictionary[user]["saldo"] - monto
                self._user_dictionary[user2]["saldo"] = self._user_dictionary[user2]["saldo"] + monto

                with open("C://Users//tonog//Documents//GitHub//POO//practica14//usuarios.json", "w") as file:
                    json.dump(self._user_dictionary, file)
                messagebox.showinfo("deposito exitoso",
                                    "tu eposito fue enviado, nuevo saldo: " + str(self._user_dictionary[user]["saldo"]))
        except KeyError:
            messagebox.showerror("ERROR", "Usuario no registrado")
