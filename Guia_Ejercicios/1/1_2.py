import math


def perimetro_rectangulo(b, h):
    return 2 * (b + h)


def area_rectangulo(b, h):
    return b * h


def area_rectangulo_coordenadas(x1, x2, y1, y2):
    arc = (x2 - x1 ) * (y2 - y1)
    return abs(arc)


def perimetro_circulo_radio(rad):
    acr = float(2 * math.pi * rad)
    return abs(acr)


def area_circulo(rad):
    return math.pi * math.pow(rad, 2)


def volumen_esfera(rad):
    return float((4 * math.pi * math.pow(rad, 3)) / 3)


def calculo_hipotenusa(cat1, cat2):
    hipotenusa = math.sqrt(cat1**2 - cat2**2)
    return hipotenusa


print('Calculo del perímetro de un rectángulo')
b = int(input('Ingrese el valor de la base : '))
h = int(input('Ingrese el valor de la altura : '))
print('El perímetro del rectángulo es :', perimetro_rectangulo(b, h), '.')
print('El área del rectángulo es :', area_rectangulo(b, h), '.')

print('\nCalculo del area mediante sus coordenadas X e Y')
x1 = int(input('Ingrese el valor de X1 : '))
x2 = int(input('Ingrese el valor de X2 : '))
y1 = int(input('Ingrese el valor de Y1 : '))
y2 = int(input('Ingrese el valor de Y2 : '))
print('El área del rectángulo es :', area_rectangulo_coordenadas(x1, x2, y1, y2), '.')

print('\nCalculo del perímetro y area de un circulo')
radio = int(input('Ingrese el valor del radio de un circulo'))
print('El perímetro del circulo es : ', perimetro_circulo_radio(radio))
print('El area del circulo es : ', area_circulo(radio))
print('El volumen de la esfera es : ', volumen_esfera(radio))

print('\nCalculo de la hipotenusa de un triangulo rectángulo')
cata = float(input('Ingrese el valor del cateto adyacente'))
catb = float(input('Ingrese el valor del cateto opuesto'))
print('La hipotenusa es : ', calculo_hipotenusa(cata, catb))
