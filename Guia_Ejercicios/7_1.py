# Escribir una funcion que reciba una tupla de elem,entos e indique si se encuentran ordenados de menor a mayor o no


def verificar_orden(tupla):
    """ recibe una tupla de elementos y verifica si esta ordenada de menor a mayor o no"""
    bandera = False

    for i in range(0, len(tupla)-1):
        print('Compara {} con {}'.format(tupla[i + 1], tupla[i]))
        if tupla[i + 1] > tupla[i]:
            bandera = True
        else:
            return False

    return bandera


# ciclo de ejecucion
mi_tupla = [11, 2, 3, 9, 5]

(verificar_orden(mi_tupla))



