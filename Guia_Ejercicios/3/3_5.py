"""
    Escribir una funcion que dada las coordenadas de un vector en r3 (X,Y,Z)
    nos devuelva la norma del vector
"""
import math


def calcular_norma_r3():
    """ Calculo de la norma de un vector """
    x, y, z = carga_vector()
    norma = math.sqrt(x**2 + y**2 + z**2)
    print('\nLa norma del vector ({},{},{}) es: {}'.format(x, y, z, norma))


def carga_vector():
    """ Carga de vectores """
    x = float(input('\nIngrese las coordenadas del vector. \nX:'))
    y = float(input('\nY:'))
    z = float(input('\nZ:'))
    return x, y, z


def diferencia_vectores():
    """ Realiza la diferencia entre dos vectores definidos en R3"""
    vector1 = carga_vector()
    vector2 = carga_vector()
    diferencia = []
    for i in range(0, 3):
        diferencia.append(float(vector1[i] - vector2[i]))
    print('\nLa diferencia de los vectores {} y {} es {}.'.format(vector1, vector2, diferencia))


def producto_vectorial():
    x1, y1, z1 = carga_vector()
    x2, y2, z2 = carga_vector()
    p_vectorial = list([(y1*z2 - z1 * y2), (x2*z1 - z2 * x1), (y2*x1 - x2 * y1)])
    return p_vectorial


# calcular_norma_r3()
# diferencia_vectores()
print('\nEl producto vectorial es: {}'.format(producto_vectorial()))
