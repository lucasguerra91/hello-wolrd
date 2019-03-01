import random


def generar_codigo():
    digitos = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    codigo = random.choice(digitos)
    for i in range(3):
        numero = random.choice(digitos)
        while numero in codigo:
            numero = random.choice(digitos)
        codigo += numero
    return codigo


print(generar_codigo())