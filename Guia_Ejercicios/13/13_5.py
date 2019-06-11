"""
Ejercicio 13.5. Escribir dos funciones mutualmente recursivas par(n) e impar(n) que deter-
minen la paridad del numero natural dado, conociendo solo que:
• 1 es impar.
• Si un número es impar, su antecesor es par; y viceversa
"""


def es_par(n):
    if n == 0:
        return True
    return es_impar(n - 1)


def es_impar(n):
    if n == 0:
        return False
    return es_par(n - 1)


# ejecucion
print(es_par(4))
print(es_impar(4))
