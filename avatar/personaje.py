class personaje:
#creamos al constructor   
  
   def __init__(self,esp,nom,alt):
      self.__especie = esp
      self.__nombre = nom
      self.__altura = alt
         
      
 #metodos correr   
   def correr(self,estado):
     if estado == True:
        print('El personaje'+self.__nombre+'esta corriendo')
     else:
        print('El personaje'+self.__nombre+'esta quieto')
        
            
  #metodo lanzar granada      
   def lanzarGranada(self):
      print('El personaje'+self.__nombre+'lanzo una granada')

   def recargarArma(self,municiones):
     cargador=5
     cargador = cargador + municiones
     print('El personaje'+self.__nombre+'recargo su arma y ahora tiene'+str(cargador)+'municiones')
    
    #Ejemplo de metodo privado 
   def __pensar(self):
      print("toy pensando. . . . ")
     
     
   #Declaramos los getters y setters de los atributos   
   def getEspecie(self):
      return self.__especie 
   
   def setEspecie(self,esp):
      self.__especie = esp 
   
   def getNombre(self):
      return self.__nombre 
   
   def setNombe(self,nom):
      self.__nombre = nom 
   
   def getAltura(self):
      return self.__altura 
   
   def setAltura(self,alt):
      self.__altura = alt 