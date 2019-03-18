"""
    Pedir al usuario una palabra , imprimirla 1000 veces en una misma linea con
    espacios, investigar sobre el parámetro end de la función print

    end = indica con que termina una orden print
    sep = nos permite agregar un separador
"""

palabra = input('Ingrese una palabra :')
for i in range(0, 10):
    print(palabra, end=' ')

for i in range(0, 10):
    print(palabra, palabra, sep=' : ')
