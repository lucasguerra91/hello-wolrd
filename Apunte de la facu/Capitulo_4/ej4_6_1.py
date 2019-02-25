def es_par(x):
    """ Verifica si el numero es par"""
    if x == 0 :
        print('Es cero')
    elif x % 2 :
        print('Es impar')
    else:
        print('Es par')


def es_primo(x):
    """ Verifica si es primo """
    

def es_primo(n):
    if n > 1:
        for i in range(2, int(n**0.5)):
            if (n % i) == 0:
                return False
        return True


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    if n < 9:
        return True
    if n % 3 == 0:
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        print('\t', f)
        if n % f == 0:
            return False
        if n % (f+2) == 0:
            return False
        f +=6
    return True


x = int(input('Ingrese un numero'))
es_par(x)

if es_primo(x):
    print('Es primo')
else:
    print('No es primo')


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
print(is_prime(x))

#contador_primos2 = 0
#for z in range(1, 1000):
#    if is_prime(z):
#        contador_primos2 += 1

#print(contador_primos2)