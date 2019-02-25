def cuadrado(x):
    return x * x

def suma_cuadrados(n):
    suma = 0
    for x in range(1, n+1):
        suma = suma + cuadrado(x)
    return suma

def hola(nombre):
    return "Hola " + nombre + "!"

def saludar():
    nombre = input("Por favor ingrese su nombre: ")
    saludo = hola(nombre)
    print(saludo)





# Separamos el ciclo de ejecucion
print("La suma de los primeros 100 cuadrados es", suma_cuadrados(100))

saludar()