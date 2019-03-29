import os
import time

PASSWORD = '123456'


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def ingreso_pass():
    """ Recibe la contraseña que ingresa el usuario """
    return input('\nPor favor ingrese la contraseña de acceso:  ')


def verifica_pass(pwd, user_pwd):
    """ Verifica la contraseña y devuelve True o False si coincide """
    if pwd == user_pwd:
        return True
    else:
        return False


# -- Ciclo de ejecución --


for i in range(3):
    user_pass = ingreso_pass()
    duracion = 5
    if user_pass == PASSWORD:
        print('Bienvenido.. \n')
        break
    else:
        if 3-(i+1) > 0:
            print('Contraseña incorrecta, le quedan ', 3-(i+1), 'intentos.. \nEspere..')
            time.sleep(duracion)
            duracion += 5
        else:
            print('Ya no le quedan intentos, vuelva mas tarde..')


if verifica_pass(PASSWORD, user_pass):
    print('\nLa contraseña coincide')
else:
    print('\nNinguna de las contraseñas ingresadas coinciden')

# os.system('pause')
