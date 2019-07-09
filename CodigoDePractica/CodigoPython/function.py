#Funcion que no regresa nada solo imprime
def decirHola(nombre=""):
  print('Hola {0}'.format(nombre))
decirHola('Andres')
decirHola()

#Funcion que me regresa un valor
def hacerSuma(num1,num2):
  total = num1 + num2
  return 'El resultado es: '+  str(total)+' '+ str( type(total)) 

num1=input('Escribe numero 1: ')
num2=input('Escribe numero 2: ')

print(hacerSuma(num1,num2))

#total= hacerSuma(2,3)
