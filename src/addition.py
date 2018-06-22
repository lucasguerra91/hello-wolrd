print("Suma de dos numeros..")
print("Precione 'q' para salir\n")

while True:
    num1 = input("Ingrese el primer valor: \n")
    if num1 == 'q':
        break
    num2 = input("Ingrese el segundo valor: \n")
    if num2 == 'q':
        break
    try:
        suma = int(num1) + int(num2)
    except TypeError:
        print("\n Deben ingresarse solo valores numericos")
    except ValueError:
        print("\n Deben ingresarse solo valores numericos")
    else:
        print("El resultado de la suma es :" + str(suma) + "\n")




