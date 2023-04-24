from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorBD:

    def __init__(self):
        pass

    #Método para crear conexiones
    def conexionBD(self):
        try: 
            conexion = sqlite3.connect("C://Users//tonog//Documents//GitHub//POO//examen_3//BDVideojuegos.db")
            print ("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
            print ("Error al conectar a la base de datos")


    #Método para guardar juego
    def guardarJuego(self, nombre, ano): 
        conx = self.conexionBD()
        if (nombre == "" or ano == ""):
            messagebox.showwarning("Campos vacíos", "Cuidaito Wasaoski, falta llenar campos")
        else:
            #3. Preparamos Cursor, Datos, QuerySQL
            cursor = conx.cursor()  
            datos = (nombre, ano)
            qrInsert = "INSERT INTO TBConsolasNintendo(nombre, ano) VALUES(?,?)"

            #4. Ejecutamos Insert y cerramos la conexión
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close() 
            messagebox.showinfo("Registro exitoso", "Juego registrado con éxito")
            
  #Método para actualizar Juego
    def actualizarJuego(self, id, nom, ano):
        #1. Preparamos la conexión
        conx = self.conexionBD()

        #2. Validar que no hayan campos vacíos
        if (id == "" or nom == "" or ano == ""):
            messagebox.showwarning("Campos vacíos", "Cuidaito Wasaoski, falta llenar campos")
        else:
            Validacion = messagebox.askyesno("Confirmación", "¿Estás seguro de actualizar el juego con el ID: " + id + " ("+nom+")?")
           
            if Validacion:
                try:#3. Preparamos el cursor, datos y query
                    cursor = conx.cursor()
                    
                    datos = (nom, ano, id)
                    qrUpdate = "UPDATE TBConsolasNintendo SET nombre = ?, ano = ? WHERE IDCNintendo = ?"
                    #4. Ejecutamos el update y cerramos la conexión
                    cursor.execute(qrUpdate, datos)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Actualización exitosa", "juego actualizado con éxito")
                except sqlite3.OperationalError:
                    messagebox.showerror("Error", "Error al intentar actualizar")
                    print ("Error al intentar actualizar")
            else:
                conx.close()
                messagebox.showinfo("Actualización cancelada", "No se actualizó el usuario")

    
    #Método para buscar jeugo
    def consultarJuego(self,id):
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
                selectQry = "SELECT * FROM TBConsolasNintendo WHERE IDCNintendo =" + id	
                #4. Ejecutamos el select y cerramos la conexión
                cursor.execute(selectQry) 
                rsUsuario = cursor.fetchall() 
                conx.close() 
                return rsUsuario

            except sqlite3.OperationalError:
                print ("Error al conectar a la base de datos")
    
    #Método para consultar a TODOS los usuarios en la BD
    def consultarTodosJuegos(self):
        #1. Preparamos la conexión
        conx = self.conexionBD()
        try:
        #2. Preparamos el cursor, datos y query
            cursor = conx.cursor()
            selectQry = "SELECT * FROM TBConsolasNintendo"
            #3. Ejecutamos el select y cerramos la conexión
            cursor.execute(selectQry)
            allUsuarios = cursor.fetchall()
            conx.close()
            return allUsuarios
        
        except sqlite3.OperationalError:
                print ("Error al consultar la BD")
                messagebox.showerror("Error", "Error al consultar la BD")

    
    #Método para eliminar usuarios
    def eliminarJuego(self, id):
        #1. Preparamos la conexión
        conx = self.conexionBD()

        #2. Validar que no hayan campos vacíos
        if (id == ""):
            messagebox.showwarning("Campos vacíos", "Por favor, es sólo un campo, llénalo por favor")
        else:
            Validacion = messagebox.askyesno("Confirmación", "¿Estás seguro de eliminar el juego con el ID: " + id + "?")
            if Validacion:
                try:
                    #3. Preparamos el cursor, datos y query
                    #3.1 Verificamos si el usuario existe en la BD
                    rsUsuario = self.consultarJuego(id)
                    if (rsUsuario == []):
                        messagebox.showwarning("Usuario no encontrado", "El usuario con el ID: " + id + " no existe")
                        return
                    else:
                        print ("Usuario encontrado")
                        cursor = conx.cursor()
                        qrDelete = "DELETE FROM TBConsolasNintendo WHERE IDCNintendo = " + id
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