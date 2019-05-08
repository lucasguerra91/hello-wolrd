import csv

# Es equivalente a usar With open
# archivo = open('archivo.txt')
# cadena = ''
# linea = archivo.readline()
# while linea != '':
#     cadena += linea
#     linea = archivo.readline()
# archivo.close()
# print(cadena)

# usando with open, nos aseguramos que se cierre correctamente
with open("archivo.txt", 'r+') as archivo:
    for i, linea in enumerate(archivo):
        # no cuenta los saltos de linea como una linea mas
        linea = linea.rstrip("\n")
        print("{}: {}".format(i, linea))
    archivo.write('\nhola')

# with open('tweets.csv') as tweets:
#     csv_reader = csv.reader(tweets)
#     for i in csv_reader:
#         print(i)

with open("saludo.py", "w") as saludo:
    saludo.write("# Este programa fue generado por otro programa!\n")
    saludo.write("print('Hola Mundo')\n")

