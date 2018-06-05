# Continuacion de lo que tengo en casa
print ' \t\t\t Asignacion de alias y copiado \n'

opuestos = {'arriba':'abajo', 'derecho':'torcido', 'verdadero':'falso'}

# Usando alias
alias = opuestos

# Usando la funcion de copiado
copia = opuestos.copy()
print '--'
print 'Se tienen la variale opuestos, su alias y una copia \n'
print 'Opuestos :' , opuestos
print 'Alias : ', alias
print 'Copia : ', copia


# Modificamos derecho dentro de alias
print '\n--'
print 'Modificamos derecho dentro de alias y vemos su comportamiento'
print
alias['derecho'] = 'sentado'
print "\t\t alias['derecho'] = 'sentado' \n"
print 'Derecho dentro de alias : \t', alias['derecho']
print 'Derecho dentro de opuestos : \t', opuestos['derecho']
print 'Derecho dentro de copia : \t',  copia['derecho']

#Modificamos derecho dentro de copia
print '\n--'
print 'Modificamos derecho dentro de copia y vemos su comportamiento'
print 
copia['derecho'] = 'privilegio'
print "\t\t copia['derecho'] = 'privilegio' \n"
print 'Derecho dentro de copia :  \t', copia['derecho'] 
print 'Derecho dentro de opuestos :  \t', opuestos['derecho'] 
print 'Derecho dentro de alias :  \t', alias['derecho']
print

# Matrices dispersas
print '----/ MATRICES /-----\n'
print 'Matriz con listas '
matriz = [
		[0,0,0,1,0],
		[0,0,0,0,0],
		[0,2,0,0,0],
		[0,0,0,0,0],
		[0,0,0,3,0] ]
	
print matriz,'\n'
print 'Matriz con diccionarios'
matriz = {(0,3):1, (2,1):2, (4,3):3}
print matriz, '\n'
print matriz[0,3]

# Esto genera un error y se usa get "print matriz[1,3]"
print matriz.get((1,3), 0)

# Pistas
print 'Serie Fibonacci \n'
anteriores = {0:1, 1:1}

def fibonacci(n):
	if anteriores.has_key(n):
		return anteriores[n]
	else:
		nuevoValor = fibonacci(n-1) + fibonacci(n-2)
		anteriores[n] = nuevoValor
		return nuevoValor

print fibonacci(50)

# Enteros largos
print '\n Enteros largos '
print type(1L)

# Contar letras
print '\nCuenta letras '
cuentaLetras = {}
for letra in "Mississippi":
	cuentaLetras[letra] = cuentaLetras.get (letra, 0) +1
print cuentaLetras
print '\nCuenta letras ordenado alfabeticamente'
# Tambien se puede organizar alfabeticamente
itemsLetras = cuentaLetras.items()
itemsLetras.sort()
print itemsLetras






