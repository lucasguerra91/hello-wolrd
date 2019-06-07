def euclides(m, n):
    r = m % n
    if r == 0:
        return n
    else:
        return euclides(n, r)


print('Ingrese el par de numeros :  ')
x = int(input('primero:'))
y = int(input('segundo:'))
mcd = euclides(x, y)
print('\nEl MCD es : ', mcd)
