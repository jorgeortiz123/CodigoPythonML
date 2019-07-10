#Codigo par ejemplificar una tienda de abarrotes
import sys
import validadortelefono
from validadortelefono import validateTel

#//////CLASE CLIENTE//////
class Cliente:
#Constructor y parametros
 def __init__(self,nombre,telefono,producto):
  self.nombre = nombre
  self.telefono = telefono
  self.producto = producto
#Inicializar variables
nombre=''
telefono=0
producto=''

print('\n' + '*Persona 1 llega a la tienda*')
nombre = input('Cliente 1 puede teclear su nombre: ')
telefono = input('Cliente 1 puede teclear su telefono: ')

print(validateTel(telefono))


producto=input('Cliente 1 puede teclear su producto a comprar: ')
#instanciar objeto
Cliente1 = Cliente(nombre,telefono,producto)

print('\n' + '*Persona 2 llega a la tienda*')
nombre = input('Cliente 2 puede teclear su nombre: ')
telefono = input('Cliente 2 puede teclear su telefono: ')
print(validateTel(telefono))

producto = input('Cliente 2 puede teclear su producto a comprar: ')
#instanciar objeto
Cliente2 = Cliente(nombre,telefono,producto)

print('\n' + '*Persona 3 llega a la tienda*')
nombre=input('Cliente 3 puede teclear su nombre: ')
telefono=input('Cliente 3 puede teclear su telefono: ')
print(validateTel(telefono))

producto=input('Cliente 3 puede teclear su producto a comprar: ')
#instanciar objeto
Cliente3 = Cliente(nombre,telefono,producto)

#Arreglo de objetos
ListaClientes = [Cliente1,Cliente2,Cliente3]

#Imprimir en un txt el nombre de los clientes
miArchivo= open ('nombreClientes.txt','w')
miArchivo.write("NOMBRE"+ "\t"+"TELEFONO"+"\t"+"PRODUCTO"+'\n')
miArchivo.write(ListaClientes[0].nombre +"\t"+ ListaClientes[0].telefono+"\t" +ListaClientes[0].producto +'\n')
miArchivo.write(ListaClientes[1].nombre +"\t"+ ListaClientes[1].telefono+"\t" +ListaClientes[1].producto +'\n')
miArchivo.write(ListaClientes[2].nombre +"\t"+ ListaClientes[2].telefono+"\t" +ListaClientes[2].producto +'\n')
miArchivo.close()
print('Datos guardados en archivo txt')
