import random


def carton():
    jugada = random.sample(range(0, 46), 6)
    return jugada


cantidad = int(input('Cuantas jugadas desea calcular? \n'))

for x in range(0, cantidad):
    print('Apuesta nro ', x + 1, ':', carton(),'\n')

print('Buena suerte!')