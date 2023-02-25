#1. Importar la clase
from personaje import *

#2. Solicitar atributos para el objeto

print('Ingrese los datos del HEROE')
especie = input('Ingrese la especie del personaje: ')
nombre = input('Ingrese el nombre del personaje: ')
altura = float(input('Ingrese la altura del personaje: '))
cargador = int(input('Ingrese la cantidad de municiones del personaje: '))
print('')
print('Ingrese los datos del ENEMIGO')
especieV = input('Ingrese la especie del personaje: ')
nombreV= input('Ingrese el nombre del personaje: ')
alturaV = float(input('Ingrese la altura del perasonaje: '))




#3. Crear el objeto

Heroe = personaje(especie,nombre,altura)
vilano = personaje(especieV,nombreV,alturaV)


#ejemplo del uso del set
Heroe.setNombe(" pepe pecas ")

#4. acceder a atributos y metodos de cada objeto

print('Los datos del heroe son: ')
print('El heroe es un '+Heroe.getEspecie()+' de nombre '+Heroe.getNombre()+' y mide '+str(Heroe.getAltura())+' metros')
print('')
print('')
print('Los datos del enemigo son: ')
print('El enemigo es un '+vilano.getEspecie()+' de nombre '+vilano.getNombre()+' y mide '+str(vilano.getAltura())+' metros')


#5. Llamar a los metodos de cada objeto

Heroe.correr(True)
Heroe.lanzarGranada()
Heroe.recargarArma(5)


#Ejemplo de lo que no se puede hacer
#Heroe.__pensar()

vilano.correr(False)
vilano.lanzarGranada()
vilano.recargarArma(5)