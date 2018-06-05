# Dedicado a importaciones
import random

# Dedicado a funciones

# Realiza el intercambio de valores entre dos tuplas
def intercambio (x,y):
	print x
	print y
	x,y= y,x
	print x
	print y
	return x,y 

# Genera una lista de numeros pseudoaleatorios
def listaAleatorios(n):
	s = [0] * n
	for i in range(n):
		s[i] = random.random()
	return s 

# Cuenta numeros 
def enElBalde(lista, minimo, maximo):
	cuenta = 0
	for num in lista:
		if minimo < num <maximo :
			cuenta+=1
	return cuenta

print "Capitulo 9 \n"
print "Tuplas \n "

#Creacion de una tupla 
tupla = ("a", "b", "c","d","e")
print "Imprimiendo tupla completa",tupla 
print "Imprimiendo tupla desde el 1 al 3", tupla[1:3]

# No se puede modificar el valor de una tupla 
# tupla[0]= "A"
# pero si se puede hacer esto
tupla = ("A",) + tupla[1:]
print "Asignando un comienzo diferente a tupla", tupla
print 
a = ("1","2")
b = ("3","4")
a,b = b,a
# seria como :
# temp = a
# a = b 
# b = temp
print a 
print b

a = ("1","2")
b = ("3","4")

print "llamando a funcion de intercambio"
print intercambio(a,b)
print 

#Numeros Aleatorios
print "Random"

for i in range(0,15):
	x = random.random() * 15
	print x
print 
print "Lista de numeros aleatorios"
lista = listaAleatorios(8)
print lista
print enElBalde(lista, 0 , 0.6)




