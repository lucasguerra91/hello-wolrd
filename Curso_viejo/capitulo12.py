print('Capitulo 12 \nClases y objetos')

# ------------------ CLASES ------------------

# Creacion de una clase o tipo
class Punto:
    pass

class Rectangulo:
    pass


# ------------------  FUNCIONES  ------------------

# Instancia como parametro
def imprimePunto(p):
    print('Los valores del punto',id(p),'son:')
    print('(' + str(p.x) + ',' + str(p.y) + ')')
# Distancia entre dos puntos
def distanciaPuntos(a,b):
    d = a.x * b.x + a.y * b.y
    return d

def mismoPunto(p1,p2):
    return (p1.x==p2.x) and (p1.y==p2.y)

def encuentraCentro(caja):
    p = Punto()
    p.x = caja.esquina.x + caja.anchura / 2.0
    p.y = caja.esquina.y + caja.altura /2.0
    return p

def agrandaRect(caja, danchura , daltura):
    caja.anchura = caja.anchura + danchura
    caja.altura = caja.altura + daltura

def mueveRect(caja, dx, dy):
    caja.esquina.x += dx
    caja.esquina.y += dy

# ------------------ COMIENZA CICLO DE EJECUCION ------------------

# A la funcion punto que crea un nuevo objeto(instacia del tipo) se lo llama constructor
blanco = Punto()
# Atributos de un objeto
blanco.x = 4.0
blanco.y = 3.0

print('Valores X e Y para blanco\n',blanco.x, blanco.y)
print('('+ str(blanco.x) + ',' + str(blanco.y)+ ')') # Otra forma de imprimir)

distanciaAlCuadrado = blanco.x * blanco.x + blanco.y * blanco.y
print('La distancia al cuadrado es de : ', distanciaAlCuadrado)

negro = Punto()
negro.x = 5
negro.y = 7
imprimePunto(negro)

print('La distancia entre los puntos blanco y negro es :',distanciaPuntos(blanco,negro),'\n')

# Mismidad
# Que dos objetos tengan los mismos valores no los hace iguales
print('Creamos dos puntos P1 y P2 y le asignamos los mismos valores.\n')
p1 = Punto()
p2 = Punto()
p1.x = 2
p1.y = 3
p2.x = 2
p2.y = 3
print('Comprobamos si son iguales y nos encontramos con que :')
if p1 == p2:
    print('Son iguales ')
else:
    print('No son iguales')

print('Ahora lo hacemos mediante la funcion mismoPunto :')
print(mismoPunto(blanco, negro),'\n\n')

print('Rectangulos')
# Instanciamos el objeto
caja = Rectangulo()
caja.anchura = 100.0
caja.altura = 200.0
# Para senalar la esquina superior izquierda, creamos un objeto dentro de otro
caja.esquina = Punto()
caja.esquina.x =  0.0
caja.esquina.y = 0.0

# Instancias como valores de retorno
centro = encuentraCentro(caja)
imprimePunto(centro)
print('\n')

# Los objetos son mudables
rec = Rectangulo()
rec.anchura = 100.0
rec.altura = 200.0
rec.esquina = Punto
rec.esquina.x = 0.0
rec.esquina.y = 0.0
print('Primer estado del rectangulo rec ')
print('Anchura del rectangulo :' ,rec.anchura)
print('Altura del rectangulo :' ,rec.altura,'\n')
agrandaRect(rec,50,100)
print('Estado del triangulo despues de agrandarlo ')
print('Anchura del rectangulo :' ,rec.anchura)
print('Altura del rectangulo :' ,rec.altura, '\n')

print('Primer posicion del rectangulo rec ')
print('Punto x de la esquina del rectangulo :' ,rec.esquina.x)
print('Punto y de la esquina del rectangulo :' ,rec.esquina.y,'\n')
mueveRect(rec,10,5)
print('Posicion del triangulo despues de moverlo')
print('Punto x de la esquina del rectangulo :' ,rec.esquina.x)
print('Punto y de la esquina del rectangulo :' ,rec.esquina.y,'\n')