# 1. Escribir una función que reciba una cadena y devuelva una tupla con la palabra que tuvo mayor
# cantidad de apariciones,
# y la cantidad de apariciones que tuvo. Si hay dos o más palabras con máxima cantidad de apariciones,
# devolver cualquiera
# de ellas. La cadena contiene únicamente palabras y espacios. Ejemplo: "la cama la silla y la mesa." -> ("la",
# 3).


def buscar_palabra_max_apariciones(cadena):
    """
    Recibe una cadena y devuelve una tupla
    :param cadena: simple cadena
    :return: una tupla (palabra , aparicion) conteniendo la palabra con mas apariciones dentro de la cadena
    """
    palabras = cadena.split(' ')
    lista = []

    for i in range(len(palabras)):
        contador = cadena.count(palabras[i])
        lista.append((palabras[i], contador))

    maximo = lista[0]

    for i in range(1, len(lista)):
        if lista[i][1] > maximo[1]:
            maximo = lista[i]
        else:
            continue

    return maximo


# ciclo de ejecucion
mi_cadena = 'Hola roberto como estas me gustaria saber como estas'
print(buscar_palabra_max_apariciones(mi_cadena))
