from pila import Pila


def calculadora_polaca(elementos):
    """ Dada una lista de elementos que representan las componentes de una expresion en
    notacion polaca inversa, evalua dicha expresion.
    Si la expresion esta mal formada, levanta ValueError """

    p = Pila()

    for elemento in elementos:
        print(f"\nDEBUG: entra {elemento}")

    # Intenta convertirlo a numero
        try:
            numero = float(elemento)
            p.apilar(numero)
            print(f"DEBUG: apila {numero}")

        # si no se puede convertir, deberia ser un operando
        except ValueError:
            if elemento not in ('+', '-', '/', '*'):
                raise ValueError("Operando inválido")

            # Si es un operando válido, intenta desapilar y operar
            try:
                a1 = p.desapilar()
                print(f"\nDEBUG: desapila {a1}")
                a2 = p.desapilar()
                print(f"\nDEBUG: desapila {a2}")
            except IndexError:
                raise ValueError("Faltan operandos..")

            if elemento == "+":
                resultado = a2 + a1

            if elemento == "-":
                resultado = a2 - a1

            if elemento == "/":
                resultado = a2 / a1

            if elemento == "*":
                resultado = a2 * a1

            print(f"\nDEBUG: apila {resultado}")
            p.apilar(resultado)

    # Al final el resultado debe ser lo unico en la pila
    resultado = p.desapilar()

    if not p.esta_vacia():
        raise ValueError("Sobran operandos")

    return resultado


def main():
    expresion = input("Ingrese la expresión a evaluar:")
    elementos = expresion.split()
    print(calculadora_polaca(elementos))


main()