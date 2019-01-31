# Capitulo 8 , Listas

lista = range (1,5)
print(lista)


vocabulario = ["mejorar", "castigar" , "defenestrar"]
numeros = [17, 123]
vacio = []

print(vocabulario, numeros, vacio)

# Acceso a los elementos
print(vocabulario[2])
print(numeros[0])

numeros[1]= 5
print(numeros)

# Imprimiendo lista
jinetes = ["guerra", "hambre", "peste", "muerte"]
i = 0
while i < len(jinetes) :
	print(jinetes[i])
	i+=1

#EJERCICIO DEL LIBRO
# Con la siguiente lista, hacer que imprima cada elemento y su longitud
lista = ["spam", 1, ["Roquefort", "Pol le Veq"],[1,2,3]]
i = 0
while i < len(lista):
	print("Elemento :", lista[i], "\n Longitud :", len(str(lista[i])), "\n\n")
	i+=1

# Verifica si un elemento pertenece a una lista
print("peste" in jinetes)
print("libertinaje" in jinetes)

#Se puede usar cualquier valor para el for, por ejemplo, verga no esta declarado
for verga in jinetes:
	print(verga)
	print("\n\n")

#Operaciones con listas
# El operador + concatena listas
a = [1,2,3]
b = [4,5,6]
c = a+b
print(c, "\n\n")

#Tambien se pueden repetir
print([0]*3)
print([1,2,3] * 3, "\n\n")

# Porciones (slices)
lista = ["a", "b","c", "d", "e", "f" ]
print(lista [1:3])
print(lista [:4])
print(lista [3:])
print(lista [:] , "\n\n")
# Funciona igual que en los arrays

#Las listas pueden modificarse
lista[1:3] = ["x", "y"]
print(lista, "\n\n")
#Se pueden borrar elementos
lista = ["a", "b","c", "d", "e", "f" ]
print(lista)
lista [1:3] = []
print(lista)
# y agregarlos nuevamente
lista [1:1] = ["b", "c"]
print(lista)

# Borrado con funcion del
a = ["uno", "dos", "tres"]
del a [1]
print(a)
lista = ['a', 'b','c','d','e','f']
# Se borra desde el primer parametro hasta uno antes del segundo parametro
del lista[1:5]
print(lista)

# Objetos 
print("OBJETOS")
a = "banana"
b = "banana"
# A y B apuntan a la misma variable
id(a); id(b)

a = [1,2,3]
b = [1,2,3];
# A y B apuntan a diferentes puntos 
id(a); id(b)

# Alias, podemos decir que utilizamos un alias cuando..
a = [1,2,3]
b = a # En este caso, a y b apuntan a lo mismo
b[0] = 5
# y los cambios que hagamos a cualquiera de los dos, afecta a los dos
print(a , "\n")


# Clonado de una lista
print("CLONADO DE LISTAS")
print("Ejercicio del Libro \n")
a = [1,2,3]
print("Valor inicial  de A = ",a)
b = []
print("Valor inicial de B = ",b, "\n")
b[:] = a[:]
print("Luego de la clonacion. \n", "Valor de A = ", a,"\n", "Valor de B = ", b, "\n")
# Luego de esto, podemos modificar b sin que afecte a A
b[1] = 8
print("Luego de modificar B. \n", "Valor de A = ", a,"\n", "Valor de B = ", b, "\n")


