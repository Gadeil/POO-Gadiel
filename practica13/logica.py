import random
import string
from tkinter import messagebox, Entry, Label
lettersmay = string.ascii_letters.upper()
lettersmin = string.ascii_letters.lower()
special_chars = string.digits + string.punctuation
1
class passwords:
    def __init__(self): 
        self.__password = "" 
        self.__len = 8 

    def createPass(self,length, mayus, special):
        if length > 0:
            self.__len = length 
        else:
            pass 
        if mayus == True and special == True:
            passPool= lettersmay+lettersmin+special_chars
        elif mayus == True and special == False:
            passPool= lettersmay+lettersmin
        elif mayus == False and special == True:
            passPool= lettersmin+special_chars
        else:
            passPool= lettersmin
        self.__password =  "".join(random.choices(passPool,k=self.__len)) 
        messagebox.showinfo("Contraseña creada",self.__password)
        
          #Aquí se crea un entry para copypastear la contraseña
        pEntry = Entry()
        pEntry.insert(0, self.__password)
        pEntry.pack()
        return self.__password
    
        
    
    #Geters y Seters
    def getLen(self): 
        return self.__len