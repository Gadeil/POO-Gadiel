from tkinter import messagebox
import sqlite3
import bcrypt


class controladorDB:
    def __init__(self):
        pass

    #Método para crear conexiones
    def conexionDB(self):
        try: 
            conexion = sqlite3.connect("C://Users//tonog//Documents//GitHub//POO//isaac//isaac.db")
            print ("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
            print ("Error al conectar a la base de datos")

     #Método para guardar usuarios
    def guardarAlumnos(self, nom, cor, con): 
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
            messagebox.showinfo("Registro exitoso", "Alumno registrado con éxito")
            
    
    def encriptarCon(self,con): 
        conPlana = con
       
        conPlana = conPlana.encode('utf-8') 
        sal = bcrypt.gensalt() 
        #encriptamos la contraseña
        conHa = bcrypt.hashpw(conPlana, sal)
        print (conHa)

        #enviamos la contraseña encriptada
        return conHa
    
    #Método para buscar Alumnos
    def consultarAlumnos(self,id):
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
    def BuscarTodoslosAlumnos(self):
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
    
    
    #Método para actualizar Alumno
    def actualizarAlumno(self, id, nom, cor, con):
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