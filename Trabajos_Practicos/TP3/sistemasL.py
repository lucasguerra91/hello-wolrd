import turtle
import os


def cargar_archivo(archivo):
    """
    Recibe el archivo del fractal, devuelve el angulo, axioma y lista de traducciones
    """

    with open(archivo, 'r')as f:
        angulo = int(f.readline())
        axioma = f.readline().rstrip('\n')
        traducciones = {}

        for linea in f:
            clave, valor = linea.split()
            traducciones[clave] = traducciones.get(clave, valor)

    return angulo, axioma, traducciones


def traducir(axioma, traducciones, cantidad):
    """

    :param axioma:  cadena que define el estado inicial
    :param traducciones: lista de traducciones predecesor - sucesor
    :return: secuencia traducida
    """
    secuencia = ''
    while cantidad > 0:
        for c in axioma:
            if c in traducciones:
                secuencia += traducciones.get(c)
            else:
                secuencia += c
        return traducir(secuencia, traducciones, cantidad - 1)
    return axioma


def dibujar_con_tortuga(secuencia, angulo):
    """

    :param secuencia:
    :param angulo:
    :return:
    """

    tortuga = turtle.Turtle()
    for c in secuencia:

        if c == 'F' or c == 'G':
            tortuga.fd(1)

        if c == 'f' or c == 'g':
            tortuga.up()
            tortuga.fd(1)
            tortuga.down()

        if c == '+':
            tortuga.rt(angulo)

        if c == '-':
            tortuga.lt(angulo)

        if c == '|':
            tortuga.rt(180)


def main(archivo, cantidad):
    """

    :return:
    """
    angulo, axioma, traducciones = cargar_archivo(archivo)
    secuencia_comandos = traducir(axioma, traducciones, cantidad)

    dibujar_con_tortuga(secuencia_comandos, angulo)


# ejecucion
main('arbol1.sl', 9)
os.system('pause')

