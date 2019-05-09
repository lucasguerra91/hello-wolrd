# Ejercicio 9.2. Diccionarios usados para contar.
# a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
# de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
# hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1} .
# b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una ca-
# dena de texto, y los devuelva en un diccionario.
# c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
# realizar y devuelva la cantidad de veces que se observa cada valor de la suma de los dos
# dados.
# Nota: utilizar el módulo random para obtener tiradas aleatorias.


def cuenta_apariciones_palabra(cadena):
    """
    :param cadena: str
    :return: un diccionario con clave: palabras valores: cantidad de apariciones en la cadena
    """
    diccionario = {}
    lista = []
    palabras = cadena.split(' ')
    # print(palabras)
    for i in range(len(palabras)):
        contador = cadena.count(palabras[i])
        lista.append((palabras[i], contador))

    for i in range(len(lista)):
        clave, valor = lista[i]

        if clave in diccionario.keys():
            continue
        else:
            diccionario[clave] = valor
    return diccionario


# ciclo de ejecucion
mi_cadena = 'We are so excited to announce Windows Terminal! Windows Terminal is a new, modern, fast, ' \
            'efficient, powerful, and productive terminal application for users of command-line tools and shells like '\
            'Command Prompt, PowerShell, and WSL.'

dic = cuenta_apariciones_palabra(mi_cadena)

for c in dic.keys():
    print(f'{c}:{dic.get(c)}')

