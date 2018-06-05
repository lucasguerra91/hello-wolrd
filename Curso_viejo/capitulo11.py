#  Copyright 2017 lguerra <lguerra@PCWX-LGUERRA>
#  capitulo11.py
  
print 'ARCHIVOS Y EXCEPCIONES '
f = open("test.dat","w")
print f

#Escribimos sobre el archivo 
f.write("Ya es hora")
f.write("de cerrar el archivo")

# Lo cerramos
f.close()

# Lo abrimos en modo lectura
f = open("test.dat","r")
print f

# Mostramos su contenido
text = f.read()
print text

# Tambien podemos indicar cuantas letras leer
f = open("test.dat","r")
print f.read(7)

print f.read(10000006)
print f.read()

# Funcion de copia de archivo

def copiaArchivo(archViejo, archNuevo):
	f1 = open(archViejo, "r")
	f2 = open(archNuevo, "w")
	while 1 :
		texto = f1.read(50)
		if texto == "":
			break
		f2.write(texto)
	f1.close()
	f2.close()
	return

print 'Prueba de copia de archivos'
copiaArchivo("test.dat","nuevo")
x = open("nuevo","r")
print x.read()


# Archivos de texto

print '\nArchivos de texto.\n'
print 'Creamos un archivo..'
f = open("test.dat","w")
f.write("linea uno\n linea dos\n linea tres\n")
f.close

print 'Lo mostramos con la funcion readline :'
f = open("test.dat","r")
print '\t-',f.readline()
print '\nLo mostramos con la funcion readlines :'
print f.readlines()

print '\nPor ultimo..'
print 'Funcion readline -\t',f.readline()
print 'Funcion readlines -\t',f.readlines(),'\n'

# Ejemplo de programa de proceso de lineas que omite las lineas 
# que empiezan con numeral

def filtraArchivo(archViejo, archNuevo):
	f1 = open(archViejo,"r")
	f2 = open(archNuevo,"w")
	while 1 :
		texto = f1.readline()
		if texto == "":
			break
		if texto[0] == "#": #si la linea comienza con numeral
			continue
		f2.write(texto)
	f1.close()
	f2.close()
	return
	
# Con esto creo cualq.dat en memoria, despues de ejecutarlo la primera 
# vez, puedo imprimirlo antes de crearlo en la segunda ejecucion
# pero ya esta en memoria
t = open("cualq.dat","w")
t.write("Aca viene el texto \n# loco")
t.close()

z = open("cualq.dat","r")
print z.read()
z.close()

filtraArchivo("cualq.dat","nuevo")
p = open("nuevo","r")
print p.read()

# Escribir variables 
print 'Escribiendo en variables con write'
x = 52

f= open("numero.dat","w")   # Aca lo abro
f.write(str(x))				# Escribo
f.close()					# Y lo cierro

f = open("numero.dat","r")	# Pero para imprimir,
print f.read()				# Lo vuelvo a abrir en r y lo imprimo

# Secuencia de formato
print '\nSecuencia de formato, pasando formato e incluyendo la variable'
motos = 52
print 'En Julio vendimos %d motos' %motos

print '%6d' % 62
print "%12.2f" % 6.1
print '\n\n\n'
# Ejemplo de como se usa para estructurar informes
print '\tInforme de tarifas\n'
def informe (tarifas):
	estudiantes = tarifas.keys()
	estudiantes.sort()
	for estudiante in estudiantes :
		print "%-20s %12.02f" % (estudiante, tarifas[estudiante])

tarifas = {'maria': 6.23, 'jose': 5.45, 'jesus':4.25}
informe(tarifas)
print '\n\n\n'

print 'Mostramos texto creado como .dat'
f = open("t1.txt","r")
print f.readline(),'\n'


# Cuando lo ejecutamos por segunda vez, es necesario usar readlines()
# porque ya agregamos texto y pisamos el original
print 'Mostramos el texto original del documento' 
s = open("C:/Users/lguerra/Desktop/texto.txt","r")
print s.readlines()
s.close()

# Modificamos el documento y lo mostramos
w = open("C:/Users/lguerra/Desktop/texto.txt","w")
w.write('\n Aca agregamos un poco mas de texto 2..')
w.close()
print '\n\nAhora mostramos el texto modificado'
s = open("C:/Users/lguerra/Desktop/texto.txt","r")
print s.readlines(), '\n'
s.close()

