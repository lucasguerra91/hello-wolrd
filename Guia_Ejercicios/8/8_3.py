# Ejercicio 8.3. Agenda simplificada
# Escribir una función que reciba una cadena a buscar y una lista de tuplas (nombre_completo,
# telefono), y busque dentro de la lista, todas las entradas que contengan en el nombre completo
# la cadena recibida (puede ser el nombre, el apellido o sólo una parte de cualquiera de ellos).
# Debe devolver una lista con todas las tuplas encontradas.


def buscar_contacto(cadena, lista):
    """
    :param cadena: el nombre o apellido (o pedazo de alguno) a buscar dentro de la lista
    :param lista: lista de nombre, telefono
    :return: nueva lista con todas las apariciones
    """
    lista_encontrados = []

    for i in range(len(lista)):
        if cadena.lower() in lista[i][0]:
            lista_encontrados.append(lista[i])

    return lista_encontrados


# ejecucion
agenda = [('Elcho', '1562347898'), ('lucas', '1562675136'), ('adri lucas', '1566080516')]
cadena_busqueda = 'Lu'
print(buscar_contacto(cadena_busqueda, agenda))

