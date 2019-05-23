def es_par(x):
    """ Verifica si el numero es par"""
    if x == 0:
        print('Es cero')
    elif x % 2:
        print('Es impar')
    else:
        print('Es par')


# def es_primo(n):
#     if n > 1:
#         for i in range(2, int(n ** 0.5)):
#             if (n % i) == 0:
#                 return False
#         return True
#     else:
#         return False


def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


x = int(input('Ingrese un numero'))
es_par(x)

if es_primo(x):
    print('Es primo')
else:
    print('No es primo')




# Sabemos por Wikipedia que existen 168 numeros primos menores a 1000 asi que lo verificamos
contador_primos = 0
for z in range(1, 1000):
    if es_primo(z):
        contador_primos += 1

print(contador_primos)
