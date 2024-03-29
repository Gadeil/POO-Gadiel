from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:

    def __init__(self):
        pass

    #Método para crear conexiones
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C://Users//tonog//Documents//GitHub//POO//tkinderSQLite//DBUsuarios.db")
            print ("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
            print ("Error al conectar a la base de datos")


    #Método para guardar usuarios
    def guardarUsuario(self, nom, cor, con): 
        conx = self.conexionBD()
        if (nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Campos vacíos", "Cuidaito Wasaoski, falta llenar campos")
        else:
            #3. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor() 
            conH = self.encriptarCon(con) 
            datos = (nom, cor, conH)
            qrInsert = "INSERT INTO TBRegistrados(nombre, correo, contra) VALUES(?,?,?)"
            

            #4. Ejecutamos Insert y cerramos la conexión
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close() 
            messagebox.showinfo("Registro exitoso", "Usuario registrado con éxito")

    def encriptarCon(self,con): 
        conPlana = con
       
        conPlana = conPlana.encode('utf-8') 
        sal = bcrypt.gensalt() 
        #encriptamos la contraseña
        conHa = bcrypt.hashpw(conPlana, sal)
        print (conHa)

        #enviamos la contraseña encriptada
        return conHa
    
    #Método para buscar usuarios
    def consultarUsuario(self,id):
        #1. Preparamos la conexión
        conx = self.conexionBD() 

        #2. Verificar si ID no está vacío
        if (id == ""): 
            messagebox.showwarning("Campos vacíos", "Cuidaito Wasaoski, falta llenar campos")
            conx.close() 
        else:
            try:
                #3. Preparamos el cursor, datos y query
                cursor = conx.cursor()
                selectQry = "SELECT * FROM TBRegistrados WHERE id =" + id	
                #4. Ejecutamos el select y cerramos la conexión
                cursor.execute(selectQry) 
                rsUsuario = cursor.fetchall() 
                conx.close() 
                return rsUsuario

            except sqlite3.OperationalError:
                print ("Error al conectar a la base de datos")
    
    #Método para consultar a TODOS los usuarios en la BD
    def consultarTodosUsuarios(self):
        #1. Preparamos la conexión
        conx = self.conexionBD()
        try:
        #2. Preparamos el cursor, datos y query
            cursor = conx.cursor()
            selectQry = "SELECT * FROM TBRegistrados"
            #3. Ejecutamos el select y cerramos la conexión
            cursor.execute(selectQry)
            allUsuarios = cursor.fetchall()
            conx.close()
            return allUsuarios
        
        except sqlite3.OperationalError:
                print ("Error al consultar la BD")
                messagebox.showerror("Error", "Error al consultar la BD")

    #Método para actualizar usuarios
    def actualizarUsuario(self, id, nom, cor, con):
        #1. Preparamos la conexión
        conx = self.conexionBD()

        #2. Validar que no hayan campos vacíos
        if (id == "" or nom == "" or cor == "" or con == ""):
            messagebox.showwarning("Campos vacíos", "Cuidaito Wasaoski, falta llenar campos")
        else:
            Validacion = messagebox.askyesno("Confirmación", "¿Estás seguro de actualizar el usuario con el ID: " + id + " ("+nom+")?")
           
            if Validacion:
                try:#3. Preparamos el cursor, datos y query
                    cursor = conx.cursor()
                    conH = self.encriptarCon(con)
                    datos = (nom, cor, conH, id)
                    qrUpdate = "UPDATE TBRegistrados SET nombre = ?, correo = ?, contra = ? WHERE id = ?"
                    #4. Ejecutamos el update y cerramos la conexión
                    cursor.execute(qrUpdate, datos)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Actualización exitosa", "Usuario actualizado con éxito")
                except sqlite3.OperationalError:
                    messagebox.showerror("Error", "Error al intentar actualizar")
                    print ("Error al intentar actualizar")
            else:
                conx.close()
                messagebox.showinfo("Actualización cancelada", "No se actualizó el usuario")
    
    #Método para eliminar usuarios
    def eliminarUsuario(self, id):
        #1. Preparamos la conexión
        conx = self.conexionBD()

        #2. Validar que no hayan campos vacíos
        if (id == ""):
            messagebox.showwarning("Campos vacíos", "Por favor, es sólo un campo, llénalo por favor")
        else:
            Validacion = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar el usuario con el ID: " + id + "?")
            if Validacion:
                try:
                    #3. Preparamos el cursor, datos y query
                    #3.1 Verificamos si el usuario existe en la BD
                    rsUsuario = self.consultarUsuario(id)
                    if (rsUsuario == []):
                        messagebox.showwarning("Usuario no encontrado", "El usuario con el ID: " + id + " no existe")
                        return
                    else:
                        print ("Usuario encontrado")
                        cursor = conx.cursor()
                        qrDelete = "DELETE FROM TBRegistrados WHERE id = " + id
                        #4. Ejecutamos el delete y cerramos la conexión
                        cursor.execute(qrDelete)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Eliminación exitosa", "Usuario eliminado con éxito")
                except sqlite3.OperationalError:
                    messagebox.showerror("Error", "Error al intentar eliminar")
                    print ("Error al intentar eliminar")
            else:
                conx.close()
                messagebox.showinfo("Eliminación cancelada", "Usuario no eliminado")