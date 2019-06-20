def ingreso_numero():
    ingreso = input("Ingrese un numero")

    try:
        numero = int(ingreso)
    except ValueError:
        print("Se debe ingresar un numero entero")
        return ingreso_numero()

    return numero


def verificar_secreto(secreto):

    ingreso_usuario = ingreso_numero()
    intentos = 1

    while ingreso_usuario != secreto:
        intentos += 1

        if ingreso_usuario > secreto:
            print("El numero ingresado es mayor al numero secreto..\n")
        else:
            print("El numero ingresado es menor al numero secreto..\n")

        ingreso_usuario = ingreso_numero()

    print(f"Felicitaciones! adivinaste el numero secreto en {intentos} intentos..!\n")


# ejecucion
n = 45
verificar_secreto(n)
