cont_ms = 0
cont_m = 0


def merge_sort3(lista):
    """ ordena una lista mediante el método merge sort
    Pre: la lista debe tener elementos comparables
    Devuelve: una nueva lista ordenada
    """
    global cont_ms
    cont_ms += 1

    if len(lista) < 2:
        return lista

    tercio = len(lista) // 3

    izq = merge_sort3(lista[:tercio])
    medio = merge_sort3(lista[tercio: (len(lista)*2)//3])
    der = merge_sort3(lista[(len(lista)*2)//3:])

    return merge(izq, medio, der)


def merge(lista1, lista2, lista3):
    """ Intercala los elementos de lista1 ,2 y 3 de forma ordenada.
    Pre: lista1 lista2 lista3 deben estar ordenadas.
    Devuelve: una lista con los elementos de lista1 , lista2 y lista3 """

    global cont_m
    cont_m += 1

    i, j, k = 0, 0, 0
    resultado = []

    while i < len(lista1) and j < len(lista2) and k < len(lista3):
        if lista1[i] < lista2[j]:
            if lista1[i] < lista3[k]:
                resultado.append(lista1[i])
                i += 1
            else:
                resultado.append(lista3[k])
                k += 1
        else:
            if lista2[j] < lista3[k]:
                resultado.append(lista2[j])
                j += 1
            else:
                resultado.append(lista3[k])
                k += 1

    # Agregar lo que falta
    resultado += lista1[i:]
    resultado += lista2[j:]
    resultado += lista3[k:]

    return resultado


# ejecucion
lista1 = [12, 24, 33, 105, 1, 15]
print(lista1)
nl = merge_sort3(lista1)
print(nl)
print('\n')


print(f"Llamadas a merge_sort :{cont_ms}")
print(f"Llamadas a merge :{cont_m}")
