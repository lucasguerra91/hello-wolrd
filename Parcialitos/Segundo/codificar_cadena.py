def codificar_cadena(cadena, diccionario):
    palabras = cadena.split()
    cadena_codificada = ''

    for i in range(len(palabras)):
        palabra_codificada = ''
        for c in palabras[i]:
            palabra_codificada += diccionario[c]
        cadena_codificada += palabra_codificada + ' '

    return palabra_codificada


# ejecucion
codificaciones = {'H': 'e', 'o': 'b', 'l': 'M', 'a': 'X'}
mi_cadena = 'Hola'
print(codificar_cadena(mi_cadena, codificaciones))
