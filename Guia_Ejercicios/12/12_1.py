import cola as c


def cola_printable(cola):
    """ Recibe una cola , devuelve una cadena con sus elementos """
    cadena = ''
    for i in range(len(cola.items)):
        if i == len(cola.items) - 1:
            cadena += str(cola.items[i])
        else:
            cadena += str(cola.items[i]) + ', '
    return cadena


class TorreDeControl:
    """ Modela  una torre de control """

    def __init__(self):
        self.arribos = c.Cola()
        self.partidas = c.Cola()

    def nueva_partida(self, vuelo):
        """ Encola un vuelo en partidas """
        self.partidas.encolar(vuelo)

    def nuevo_arribo(self, vuelo):
        """ Encola un vuelo en arribos """
        self.arribos.encolar(vuelo)

    def ver_estado(self):
        """ Imprime el estado actual de las colas: arribos y partidas """
        if self.arribos.esta_vacia():
            print(f"\nNo hay vuelos esperando para aterrizar.")
        else:
            print(f"\nVuelos esperando para aterrizar : {cola_printable(self.arribos)}")

        if self.partidas.esta_vacia():
            print(f"No hay vuelos esperando para despegar.")
        else:
            print(f"Vuelos esperando para despegar : {cola_printable(self.partidas)}")

    def asignar_pista(self):
        """ Desencola el primer vuelo dentro de arribos, en caso de estar vacia la cola
        de arribos, desencola el primer vuelo dentro de partidas.
        Si ambas están vacias, lo informa.."""

        if not self.arribos.esta_vacia():
            vuelo = self.arribos.desencolar()
            print(f"\nEl vuelo {vuelo} aterrizó con éxito.")
            return

        if not self.partidas.esta_vacia():
            vuelo = self.partidas.desencolar()
            print(f"\nEl vuelo {vuelo} despegó con éxito.")
            return

        print(f"\nNo hay vuelos en espera.")


torre = TorreDeControl()

torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()

torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()

torre.ver_estado()