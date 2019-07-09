x = 10
y = 5
if x > y:
  print('{0} es mas grande que {1}'.format(x,y))
else: 
  print('{0} es mas grande que {1}'.format(y,x))

print ('------------') 

if x > y:
  print ('{0} es mas grande que {1}'.format(x,y))
elif x==y:
  print('{0} y {1} son iguales '.format(x,y))
else:
  print('{0} es menor que {1}'.format(x,y))


#if aninados 
if x > 2:
 if x <= 10:
  print ('{0} es mas grande que 2 e igual/menor a 10'.format(x))


if x > 2 and x<=10:
  print ('{0} es mas grande que 2 e igual/menor a 10'.format(x))



if x>2 or x<=10:
  print ('{0} es mas grande que 2 e igual/menor a 10'.format(x))

if not(x==y):
  print('{0} es igual a {1}'.format(x,y))
