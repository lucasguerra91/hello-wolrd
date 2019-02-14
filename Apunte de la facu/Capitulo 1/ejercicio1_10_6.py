# Implementar un algoritmo que dado un numero n permita calcular el factorial
def factorial(num):
    fact = 1
    for i in range(1, num):
        fact += fact * i
    return fact


numero = int(input('Ingrese un numero'))
print('Su factorial es :', factorial(numero))
