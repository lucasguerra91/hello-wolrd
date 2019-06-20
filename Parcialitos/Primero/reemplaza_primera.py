def reemplaza_primera(cadena):
    """
    Reemplaza todas las apariciones de la primer letra de la cadena por ?
    :param cadena: de caracteres
    :return: una nueva cadena producto de aplicar las transformaciones. Si se ingresa
    una cadena vacia , se devuelve una nueva con un solo ?
    """

    if len(cadena) == 0:
        return '?'

    primera = cadena[0].lower()
    aux = ''

    for letra in cadena:
        if letra.lower() == primera:
            aux += '?'
        else:
            aux += letra

    return aux


# ejecucion
ingreso = input("ingrese una cadena...")
ingreso_transformado = reemplaza_primera(ingreso)
print(f"Usted ingresó:\n {ingreso}\n Transformada queda como:\n {ingreso_transformado}")
