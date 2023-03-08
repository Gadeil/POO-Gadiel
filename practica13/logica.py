import string,secrets

# class logica:
#     def __init__(self,letra,digito,cara):
#         self.__letras=letra
#         self.__digitos=digito
#         self.__caracEsp=cara
       
    

letras = string.ascii_letters
digitos = string.digits
caracEsp = string.punctuation

automatico= letras + digitos + caracEsp 

rango = 8

pwd = ''
for i in range(rango):
 pwd += ''.join(secrets.choice(automatico))
print(pwd)

def contra ():
    pwd = ''
    for i in range (rango):
     pwd += ''.join(secrets.choice(automatico))
    
     if (any(char in caracEsp for char in pwd) and 
      sum(char in digitos for char in pwd)>=2):
          break
    print(pwd)


