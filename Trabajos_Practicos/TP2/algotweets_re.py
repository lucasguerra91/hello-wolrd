import sys
import csv
import random
import time
import datetime


def random_choice(d):
    """ A partir de un diccionario , genera una clave utilizando sus valores como referencia
    para el calculo de probabilidad de ser elegida, devuelve la clave """
    clave_random = random.choices(list(d), weights=d.values())
    clave = clave_random[0]
    return clave


def generar_diccionarios(usuarios):
    """ Recibe una lista de usuarios y a partir de ellos genera 3 diccionarios de palabras:
    iniciales , proximas y finales. Retorna los 3 diccionarios. """

    dic_tws = {}
    dic_p_inicial = {}
    dic_p_final = {}
    dic_p_prox = {}
    with open('tweets.csv', encoding="utf8", ) as f:
        tweets_csv = csv.reader(f, delimiter='\t')

        for tweet in tweets_csv:
            if tweet[0] in usuarios:
                dic_tws.setdefault(tweet[0], [tweet[1]]).append(tweet[1])

    for usuario in dic_tws:

        for tweet in dic_tws[usuario]:

            lista = tweet.split()
            dic_p_inicial[lista[0]] = dic_p_inicial.get(lista[0], 0) + 1

            for i in range(len(lista)):
                if i + 1 < len(lista):
                    if lista[i] in dic_p_prox:
                        if lista[i + 1] in dic_p_prox[lista[i]]:
                            dic_p_prox[lista[i]][lista[i + 1]] += 1
                        else:
                            dic_p_prox.setdefault(lista[i], {}).setdefault(lista[i + 1], 1)
                    else:
                        dic_p_prox.setdefault(lista[i], {}).setdefault(lista[i + 1], 1) + 1
                else:
                    dic_p_final[lista[i]] = dic_p_final.get(lista[i], 0) + 1

    return dic_p_inicial, dic_p_prox, dic_p_final


def mostrar_favoritos(cantidad):
    """
    Imprime los tweets que fueron guardados como favoritos, si la cantidad es mayor a los tweets guardados
    se imprimirán todos.
    :param cantidad: de favoritos que se desea mostrar.
    :print: favoritos ordenados por mas recientes .
    """
    lista_fav = []
    contador = 0

    if cantidad > 0:
        with open('favoritos.csv', 'r', encoding='utf-8') as f:
            favoritos_csv = reversed(list(csv.reader(f, delimiter='\t')))
            for tweet in favoritos_csv:
                if contador < cantidad:
                    lista_fav.append(str(tweet[1]).rstrip(','))
                    contador += 1
                else:
                    break
        print(f"\nÚltimos {cantidad} favoritos: \n")
        for i in range(len(lista_fav)):
            print(f"- {lista_fav[i]} \n")

    elif cantidad == 0:
        with open('favoritos.csv', 'r', encoding='utf-8') as f:
            favoritos_csv = reversed(list(csv.reader(f, delimiter='\t')))
            for tweet in favoritos_csv:
                lista_fav.append(tweet[1])

        print(f"\nLista de favoritos ordenados por mas reciente: \n")
        for i in range(len(lista_fav)):
            print(f"- {lista_fav[i]} \n")


def mostrar_trending(cantidad):
    """
    Recibe como parametro la cantidad de #hashtags con mayor aparicion que el usuario desea visualizar y los
    muestra en pantalla
    :param cantidad: numero entero (controlado antes de entrar). Cero para imprimir todos
    :return:Imprime los $cantidad de hashtags mas utilizados,si $cantidad > len(tweets) o $cantidad = 0 : imprime todos
    """
    tt = {}
    lista_hashtags = []

    with open('tweets.csv', encoding="utf8", ) as f:
        tweets_csv = csv.reader(f, delimiter='\t')

        for tweet in tweets_csv:
            palabras = tweet[1].split()

            for i in range(len(palabras)):
                if palabras[i].startswith('#'):
                    lista_hashtags.append(palabras[i])

    for i in range(len(lista_hashtags)):
        if lista_hashtags[i] in tt:
            tt[lista_hashtags[i]] += 1
        else:
            tt[lista_hashtags[i]] = 1

    lista_hashtags_ordenada = list(sorted(tt, key=tt.get, reverse=True))

    print(f"\nEste es el top {cantidad} de #hashtags: \n")
    if cantidad > len(lista_hashtags_ordenada):
        for i in range(len(lista_hashtags_ordenada)):
            print(' ' + lista_hashtags_ordenada[i] + '\n')
    else:
        for i in range(cantidad):
            print(' ' + lista_hashtags_ordenada[i] + '\n')
    print('\n')


def generar_tweet(usuarios):
    """
    Genera un tweet en base a tweets anteriores de los usuarios indicados por consola
    :param usuarios: lista de los usuarios en base a los cuales se genera el tweet
    :return: se imprime el tweet generado y se pregunta si se lo quiere agregar a favoritos
    """
    tweet_generado = ''
    aux = {}
    usuarios_totales = []
    longitud_tw = random.randrange(90, 280)
    hora_actual = str(datetime.datetime.now())

    try:

        if len(usuarios) == 0:
            with open('tweets.csv', encoding="utf8", ) as f:
                tweets_csv = csv.reader(f, delimiter='\t')
                for linea in tweets_csv:
                    aux[linea[0]] = 1

            for usuario in aux.keys():
                usuarios_totales.append(usuario)

            usuarios = usuarios_totales

        iniciales, proximas, finales = generar_diccionarios(usuarios)

        usuarios_printable = ''

        for idx in range(len(usuarios)):
            usuarios_printable += usuarios[idx] + ' - '

        print(f"\nGenerando tweet a partir de : {usuarios_printable}...\n")

        primer_palabra = random_choice(iniciales)
        tweet_generado += primer_palabra
        proxima_palabra = random_choice(proximas[primer_palabra])

        tweet_generado += ' ' + proxima_palabra

        while len(tweet_generado) < longitud_tw:
            # print('entro al while..')
            if proxima_palabra in proximas:
                proxima_palabra = random_choice(proximas[proxima_palabra])
                tweet_generado += ' ' + proxima_palabra
            else:
                proxima_palabra = random_choice(proximas[primer_palabra])

        tweet_generado += '.'
        print(tweet_generado)
        guardar = input('\nDesea guardar el tweet como favorito? [s/n] ')

        if guardar == 's':
            with open('favoritos.csv', 'a', encoding='utf-8') as f:
                # favoritos_csv = csv.writer(f)
                f.write(hora_actual + '\t' + tweet_generado + '\n')
            print(f"\nTweet guardado con éxito.!")
        elif guardar == 'n':
            print(f"\nHasta luego..")
            # else:
            #     raise Exception
    except IndexError:
        print(f"[ATENCIÓN]El usuario ingresado no se encuentra en la lista...")


def main():
    try:

        if sys.argv[1] == 'trending':
            try:
                if int(sys.argv[2]) < 0:
                    raise Exception
                mostrar_trending(int(sys.argv[2]))
            except IndexError:
                print(f"[ATENCIÓN]Para utilizar la función trending es obligatorio indicar la cantidad de hashtags")
            except ValueError:
                print(f"[ATENCIÓN]Se debe ingresar un numero entero.")
            except:
                print(f"[ATENCIÓN]A que jugas? El numero entero ingresado debe ser positivo u.u ")

        elif sys.argv[1] == 'generar':
            lista_usuarios = []
            for i in range(2, len(sys.argv)):
                lista_usuarios.append(sys.argv[i])

            generar_tweet(lista_usuarios)

        elif sys.argv[1] == 'favoritos':
            if len(sys.argv) == 2:
                mostrar_favoritos(0)
            elif int(sys.argv[2]) > 0:
                mostrar_favoritos(int(sys.argv[2]))

        else:
            print(f"\n[ATENCIÓN]")
            print(f"\nDebe introducir alguna de las siguientes funciones: \n"
                  f"\t* trending <cantidad de hashtags>\n"
                  f"\t* generar <usuario1> <usuarioN> - De no ingresar usuario se genera tweet en base a toda la db\n"
                  f"\t* favoritos <cantidad de tweets>\n")

    except UnicodeEncodeError:
        print(f"\n[ATENCIÓN]")
        print(f"Algunos caracteres animados no pudieron ser cargados.\n")
    except:
        print(f"\n[ATENCIÓN]")
        print(f"\nDebe introducir alguna de las siguientes funciones: \n"
              f"\t* trending <cantidad de hashtags>\n"
              f"\t* generar <usuario1> <usuarioN> - De no ingresar usuario se genera tweet en base a toda la db\n"
              f"\t* favoritos <cantidad de tweets>\n")

# ejecucion
main()





