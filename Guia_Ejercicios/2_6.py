"""
    EScribir un programa que tome una cantidad m de valores ingresados
    por el usuario , a cada uno le calcule el factorial, imprima
    el resultado junto con el numero de orden correspondiente
"""


def calcular_factorial(num):
    fact = 1
    for i in range(1, num):
        fact += fact * i
    return fact


def leer_centinela():
    return input('\nIngrese un número (* para terminar) :')


def calcular_factoriales():
    centinela = leer_centinela()
    f = []

    while centinela != '*':
        f.append(calcular_factorial(int(centinela)))
        centinela = leer_centinela()

    for i in range(len(f)):
        print(i+1, '-', f[i])


calcular_factoriales()
