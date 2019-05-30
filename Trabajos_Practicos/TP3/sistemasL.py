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


def main(archivo, cantidad):
    """

    :return:
    """
    angulo, axioma, traducciones = cargar_archivo(archivo)
    secuencia_comandos = traducir(axioma, traducciones, cantidad)

    print(secuencia_comandos)


# ejecucion
main('sier2.sl', 2)


