from tkinter import messagebox
import sqlite3

import bcrypt



class ControladorBD():

    def __init__(self):
        pass

    # metodo para crear conexiones
    def conexionBd(self):
        try:
            conexion = sqlite3.connect("C:/Users/tonog/Documents/GitHub/POO/tkinderSQLite/DBUsuarios.db")
            print("conectado a la BD")
            return conexion

        except sqlite3.OperationalError:
            print("no se puedo conectar")

    # metodos para guardar usuarios    

    def guardarUsuario(self, nom, cor, con):

        # 1. usamos una conexion
        conx = self.conexionBd()
        print(conx)

        # 2. validar parametros vacios
        if (nom == "" or cor == "" or con == ""):
            messagebox.showwarning("agua", "formulario incompleto")
            print("aqui")
        else:

            # 3. preparamos cursor, datos, querysql
            cursor = conx.cursor()
            conH = self.encriptarCon(con)
            datos = (nom, cor, conH)
            qrInsert = "insert into TBRegistrados(nombre, correo, contra) values (?,?,?)"
            # 4. ejecutar insert y cerramos conexion
            cursor.execute(qrInsert, datos)

            # 4. ejecutar insert y cerramos conexion
            # print(cursor.execute(qrInsert))
            # cursor.execute(qrInsert)
            conx.commit()
            conx.close
            messagebox.showinfo("exito", "usuario guardado")

    # Metodo para encriptar contraseñas
    def encriptarCon(self, con):

        # conPlana = con
        #
        # conPlana = conPlana.encode()  # convertimos con a bytes
        # salt = bcrypt.gensalt()
        # conHa = bcrypt.hashpw(conPlana, salt)
        # print(conHa)
        return con
