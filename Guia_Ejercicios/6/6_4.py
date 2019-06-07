CARACTER = '.'


def inserta_en_digitos(cadena):
    ''' Recibe una cadena larga de numeros enteros y devuelve una nueva cadena con las separaciones
    por unidades de miles / millones / etc (. cada 3 cifras) '''
    new_cadena = ''
    limite = len(cadena) - 1

    for i in range(0, len(cadena)):
        if (limite - i) > 0 and (limite - i) % 3 == 0:
            new_cadena += cadena[i] + CARACTER
        else:
            new_cadena += cadena[i]
    return new_cadena


mi_cadena = input('Ingrese la cadena de numeros enteros:')
print(inserta_en_digitos(mi_cadena))
