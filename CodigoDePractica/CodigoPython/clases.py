#Create a class
class Usuario:
 #Constructor()
 def __init__(self,nombre,email,edad):
  self.nombre = nombre
  self.email = email
  self.edad = edad

 def saludos(self):
  return 'Me llamo {0} y tengo {1}'.format(self.nombre,self.edad)

 def tengo_cumple(self):
  self.edad+=1

#class Cliente(Usuario):
#Andres = Usuario('Jorge','jorge@Gmail.com',19)
#print(type(Andres))
#print(Andres.nombre)
#print(Andres.email)
#print(Andres.saludos())

#	CLASE CLIENTE
class Cliente(Usuario):
 #Constructor()
 def __init__(self,nombre,email,edad):
  self.nombre = nombre
  self.email = email
  self.edad = edad
  self.saldo = 0

 def establecerSaldo(self,saldo):
  self.saldo=saldo

 def saludos(self):
   return 'Me llamo {0} y tengo {1}'.format(self.nombre,self.edad)


#Instanciar el objeto cliente
Rufina_Usuario = Usuario('Rufina Madrid','rufina@htomail.com',2)
Rufina_Cliente = Cliente('Rufina Madrid','rufina@htomail.com',2)



Rufina_Cliente.establecerSaldo(50000)
print(Rufina_Cliente.saludos())
print(Rufina_Usuario.saludos())

