import os
import logica as l
import sys


parametros = sys.argv


def main():
    """

    """
    _, archivo, cantidad, destino = parametros

    try:
        if not len(parametros) == 4:
            raise IndexError

        if not os.path.isfile(archivo):
            raise FileExistsError

        # if not int(sys.argv[2]) > 0:
        #     raise TypeError

        if not destino:
            raise ValueError
        else:
            if not str(destino).lower().endswith('.svg'):
                destino += ".svg"

        angulo, axioma, traducciones = l.cargar_archivo(archivo)
        secuencia_comandos = l.traducir(axioma, traducciones, int(cantidad))

        l.crear_svg(destino, secuencia_comandos, angulo)
        print(f'Se creó con éxito el archivo {destino} a partir del fractal {archivo}.\n Hasta luego..')
    except IndexError:
        print(f"La cantidad de argumentos no es la correcta.")
    except FileExistsError:
        print(f"El archivo de origen ingresado no existe, reviselo e intete nuevamente.")
    # except TypeError:
    #     print(f"La cantidad ingresada debe ser un numero positivo")
    except ValueError:
        print(f"La extensión del archivo de destino debe ser .svg")
    except NameError as e:
        print(e)


# ejecucion
main()
os.system('pause')
