
from tkinter import Tk,Frame,Button,messagebox,Entry,Label
 
class logica:
  def __init__(self,cor,con):
     self.__correo=cor
     self.__contraseña=con

  def correov (self,cor,con):
       correo=input(str("ingresa el correo: "))
       contraseña=input(str("Ingresa tu contraseña"))
       if correo == "tonogar@gmail.com" and contraseña == "12345":
           messagebox.showinfo("aviso","bienvenido")
       else: 
          messagebox.showinfo("aviso","Error")
      

      
 
 
   
   




