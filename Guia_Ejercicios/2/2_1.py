capital = int(input('Ingrese el monto del capital inicial :'))
interes = int(input('Ingrese la tasa de interés :'))
anos = int(input('Ingrese la cantidad de años :'))

monto_final = capital * (1+ ( interes /100)) * anos
print('El importe final sera de :', monto_final)