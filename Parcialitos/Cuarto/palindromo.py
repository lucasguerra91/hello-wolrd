def es_palindromo(cadena):
    """
    Verifica si una cadena es palindromo
    :param cadena: sin caracteres especiales , solo espacios (?)
    :return: True o False
    """
    c = cadena.replace(" ", "")

    fin = len(c) - 1

    if len(c) <= 1:
        return True

    if c[0] != c[fin]:
        return False

    return es_palindromo(c[1: fin])


# ejecucion
cadena1 = "amargor pleno con el programa"

if es_palindromo(cadena1):
    print("Es palindromo")
else:
    print("No es palindromo")