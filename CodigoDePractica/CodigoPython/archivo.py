#Abrir Archivo
miArchivo= open ('miArchivo.txt','w')

#Obtener info del archivo
print('Name: ',miArchivo.name)
print('Esta Cerrado: ', miArchivo.closed)
print('Modo abierto: ',miArchivo.mode)

#Escribir algo al archivo
miArchivo.write('ASDFH')
miArchivo.write('Y root')
miArchivo.close()

#Agregar al Archivo
miArchivo = open('miArchivo.txt','a')
miArchivo.write('ahsjdh')
miArchivo.close()

#Leer Archivo
miArchivo = open ('miArchivo.txt','a')
texto = miArchivo.read(100)
print(texto)
