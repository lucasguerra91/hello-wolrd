from string import ascii_lowercase


def verificar_pangrama(cadena):
    """Recibe una cadena y verifica si la misma es un pangrama, devolviendo True o False"""
    for i in range(len(ascii_lowercase)):
        if ascii_lowercase[i] in cadena.lower():
            continue
        else:
            return False
    return True


cadena_test = 'the quick brown fox jumps over the lazy dog'

if verificar_pangrama(cadena_test):
    print('La cadena es un pangrama.')
else:
    print('La cadena no es un pangrama.')