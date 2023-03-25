from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    
    def __init__(self):
        pass
    # metodo para crear conexiones
    def conexionBd(self):
        try:
            conexion=sqlite3.connect("C:/Users/tonog/Documents/GitHub/POO/tkinderSQLite/DBUsuarios.db")
            print("conectado a la BD")
            return conexion
          
        except sqlite3.OperationalError:
            print("no se puedo conectar")
        
    # metodos para guardar usuarios    
    
    def guardarUsuario(self,nom,cor,con):
        
        #1. usamos una conexion 
        conx=self.conexionBd()
        
        #2. validar parametros vacios 
        if(nom== "" or cor== "" or con=="" ):
            messagebox.showwarning("agua", "formulario incompleto")
        else:
            
            #3. preparamos cursor, datos, querysql
            cursor = conx.cursor()
            conH= self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(nombre, correo, contra)"
        
            #4. ejecutar insert y cerramos conexion
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close
            messagebox.showinfo("exito","usuario guardado")
            
     #Metodo para encriptar contraseñas       
    def encriptarCon(self,con):
        conPlana= con
        
        conPlana= conPlana.encode() #convertimos con a bytes
        sal= bcrypt.gensalt()
        conHa= bcrypt.hashpw(conPlana,sal)
        print(conHa)
        return conHa