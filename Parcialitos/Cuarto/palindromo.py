def es_palindromo(cadena):
    """

    :param cadena:
    :return:
    """
    fin = len(cadena) - 1
    inicio = 0

    if len(cadena) == 1:
        return 
    if cadena[inicio] != cadena[fin]:
        return False

    return es_palindromo(cadena[inicio + 1: fin - 1])


# ejecucion
cadena = "arepera"
if es_palindromo(cadena):
    print("Es palindromo")
else:
    print("No es palindromo")