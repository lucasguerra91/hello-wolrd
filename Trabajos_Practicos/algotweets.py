import sys
import csv
import random
import time


# print(sys.argv[0])
# print(sys.argv[1])


def random_choice(d):
    clave_random = random.choices(list(d), weights=d.values())
    clave = clave_random[0]
    return clave


def mostrar_trending(cantidad):
    """
    Recibe como parametro la cantidad de #hashtags con mayor aparicion que el usuario desea visualizar y los
    muestra en pantalla
    :param cantidad:
    :return:
    """
    tt = {}
    lista_hashtags = []

    # armo una lista de hashtags
    with open('tweets.csv', encoding="utf8", ) as f:
        tweets_csv = csv.reader(f, delimiter='\t')

        for tweet in tweets_csv:
            palabras = tweet[1].split()

            for i in range(len(palabras)):
                if palabras[i].startswith('#'):
                    lista_hashtags.append(palabras[i])

    for i in range(len(lista_hashtags)):
        if lista_hashtags[i] in tt.keys():
            tt[lista_hashtags[i]] += 1
        else:
            tt[lista_hashtags[i]] = 1

    # [:cantidad] con esto le pongo limite a la lista pero no me queda presentable para imprimir
    lista_hashtags_ordenada = list(sorted(tt, key=tt.get, reverse=True))
    print(len(lista_hashtags_ordenada))

    if cantidad > len(lista_hashtags_ordenada):
        for i in range(len(lista_hashtags_ordenada)):
            print(lista_hashtags_ordenada[i])
    else:
        for i in range(cantidad):
            print(lista_hashtags_ordenada[i])


def generar_tweet(usuarios):
    """

    :param usuarios: lista de los usuarios en base a los cuales se genera el tweet
    :return: se imprime el tweet generado y se pregunta si se lo quiere agregar a favoritos
    """
    # Diccionario de tweets {<usuario>: [tweets]}
    dic_tws = {}

    # Diccionario de palabras iniciales {<palabra> : cantidad de apariciones (al inicio)}
    dic_p_inicial = {}

    # Diccionario de palabras iniciales {<palabra> : cantidad de apariciones (al inicio)}
    dic_p_final = {}

    # Diccionario de proximas palabras {<palabra> : {<palabra_sgte> : apariciones }}
    dic_p_prox = {}

    tweet_generado = ''
    aux = {}
    usuarios_totales = []
    # Para hacerlo un poco mas realista, nadie escribe ni menos de 40 ni siempre los 280 caracteres
    longitud_tw = random.randrange(40, 280)

    try:
        # ----------------- POR SI LA LISTA VIENE VACIA ------------------------
        with open('tweets.csv', encoding="utf8", ) as f:
            tweets_csv = csv.reader(f, delimiter='\t')
            for linea in tweets_csv:
                aux[linea[0]] = 1

        for usuario in aux.keys():
            usuarios_totales.append(usuario)

        if len(usuarios) == 0:
            usuarios = usuarios_totales
        # ------------------- ES MEDIO REBUSCADO --------------------------------

        for usuario in usuarios:

            dic_tws_usuario = {}

            with open('tweets.csv', encoding="utf8", ) as f:
                tweets_csv = csv.reader(f, delimiter='\t')

                for tweet in tweets_csv:
                    if tweet[0] == usuario:
                        if usuario in dic_tws_usuario.keys():
                            dic_tws_usuario[usuario].append(tweet[1])
                            continue
                        else:
                            dic_tws_usuario[usuario] = [tweet[1]]

            dic_tws.update(dic_tws_usuario)

        for usuario in dic_tws.keys():
            for tweet in dic_tws[usuario]:
                lista = tweet.split()
                # print(lista)
                # Armo el diccionario con las palabras iniciales y sus apariciones
                if lista[0] in dic_p_inicial.keys():
                    dic_p_inicial[lista[0]] += 1
                    # print(f"LOGG - se sumo 1 a {lista[0]} en dic inicial")
                else:
                    dic_p_inicial[lista[0]] = 1
                    # print(f"LOGG - se creo {lista[0]} en dic inicial")

                # Armo los dos diccionarios restantes
                for i in range(len(lista)):
                    # print(f"LOGG - entro al for de la lista")

                    if i + 1 < len(lista):
                        if lista[i] in dic_p_prox.keys():
                            if lista[i + 1] in dic_p_prox[lista[i]].keys():
                                dic_p_prox[lista[i]][lista[i + 1]] += 1
                                # print(f"LOGG -se sumo uno a {lista[i + 1]} en {lista[i]} dic prox")
                            else:
                                dic_p_prox[lista[i]][lista[i + 1]] = 1
                                # print(f"LOGG - se guardo {lista[i+1]} en {lista[i]} dic prox")
                        else:
                            dic_p_prox[lista[i]] = {lista[i + 1]: 1}
                            # print(f"LOGG - se guardo [{lista[i + 1]}  {lista[i]}] en dic prox")

                    else:
                        if lista[i] in dic_p_final.keys():
                            dic_p_final[lista[i]] += 1
                        else:
                            dic_p_final[lista[i]] = 1

        with open('primeras.txt', 'w', encoding='utf-8') as f:
            for clave in dic_p_inicial.keys():
                f.write(clave + ':' + str(dic_p_inicial[clave]) + '\n')

        with open('proxima.txt', 'w', encoding='utf-8') as f:
            for clave in dic_p_prox.keys():
                f.write(f"{clave}:\t{dic_p_prox[clave]}\n")

        usuarios_printable = ''

        for i in range(len(usuarios)):
            usuarios_printable += usuarios[i] + ' - '

        print(f"Generando tweet a partir de : {usuarios_printable}...")
        time.sleep(2)

        primer_palabra = random_choice(dic_p_inicial)
        tweet_generado += primer_palabra

        proxima_palabra = random_choice(dic_p_prox[primer_palabra])

        # print(f"DEBUGG - Proxima palabra : {proxima_palabra}")

        tweet_generado += ' ' + proxima_palabra

        while len(tweet_generado) < longitud_tw:
            # print('entro al while..')
            if proxima_palabra in dic_p_prox.keys():
                proxima_palabra = random_choice(dic_p_prox[proxima_palabra])
                tweet_generado += ' ' + proxima_palabra
            else:
                break
        tweet_generado += '.'

        print(tweet_generado)
        guardar = input('Desea guardar el tweet como favorito? [s/n] ')

        # while guardar != 's' or guardar != 'n':
        #     guardar = input('Desea guardar el tweet como favorito? s/n ')

        if guardar == 's':
            with open('favoritos.csv', 'a', encoding='utf-8') as f:
                # favoritos_csv = csv.writer(f)
                f.write(tweet_generado + '\n')
            print(f"\nTweet guardado con éxito.!")
    except IndexError:
        print(f"El usuario ingresado no se encuentra en la lista...")



# ejecucion
try:
    if sys.argv[1] == 'trending':
        try:
            if int(sys.argv[2]) < 0:
                raise Exception
            mostrar_trending(int(sys.argv[2]))
        except IndexError:
            print(f"Para utilizar la función trending es obligatorio indicar la cantidad de hashtags")
        except ValueError:
            print(f"Se debe ingresar un numero entero.")
        except:
            print(f"A que jugas? El numero entero ingresado debe ser positivo u.u ")

    elif sys.argv[1] == 'generar':
        lista_usuarios = []
        for i in range(2, len(sys.argv)):
            lista_usuarios.append(sys.argv[i])

        generar_tweet(lista_usuarios)

    else:
        raise Exception
except IndexError:
    print(f"\nDebe introducir alguna de las siguientes funciones: \n"
          f"\t* trending <cantidad de hashtags>\n"
          f"\t* generar <usuario1> <usuarioN> - De no ingresar usuario se genera tweet en base a toda la db\n"
          f"\t* favoritos <cantidad de tweets>\n")

#generar_tweet(['_ErnestoSabato', 'erescurioso'])


