import os


def calcula_absoluto(n):
    if n < 0:
        return n * (-1)
    return n


def ingresa_numero():
    numero = input('Ingrese un numero, * Para terminar: ')
    return numero


def borra_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


numero_usuario = ingresa_numero()

while numero_usuario != '*':
    borra_pantalla()
    if numero_usuario.lstrip('-').isdigit():
        print(calcula_absoluto(int(numero_usuario)))
    else:
        print('Solo funciona con numeros..!')
    numero_usuario = ingresa_numero()
