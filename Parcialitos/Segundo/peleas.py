def validar_numero(valor):
    if not isinstance(valor, (int, float, complex)):
        raise TypeError(f"{valor} no es un valor numerico")
    return valor


def validar_cadena(valor):
    if not isinstance(valor, str):
        raise TypeError(f"{valor} no es una cadena")
    return valor


class Pelea:
    """
        define un street fighter
    """

    def __init__(self, retador, defensor):
        self.retador = validar_cadena(retador)
        self.defensor = validar_cadena(defensor)
        self.ptos_retador = 0
        self.ptos_defensor = 0
        self.ganador = ''

    def cargar_resultado(self, ptos_retador, ptos_defensor):
        self.ptos_retador = validar_numero(ptos_retador)
        self.ptos_defensor = validar_numero(ptos_defensor)

    def obtener_ganador(self):

        if self.ptos_retador > self.ptos_defensor:
            self.ganador = self.retador
        elif self.ptos_defensor > self.ptos_retador:
            self.ganador = self.defensor
        else:
            self.ganador = 'TIE'

        return self.ganador


class HistorialDePelea:
    """  """

    def __init__(self):
        self.historial = {}
        self.ganador_record = ''

    def cargar_pelea(self, pelea):
        try:
            if pelea.ganador != 'TIE':
                if pelea.ganador in self.historial.keys():
                    self.historial[pelea.ganador][0] += 1
                else:
                    self.historial[pelea.ganador] = [1]
            else:
                raise Exception
        except:
            print(f'No se cargan los empates')

    def obtener_record(self):
        peleas_ganadas = 0

        for peleador in self.historial.keys():
            if int(self.historial[peleador][0]) > peleas_ganadas:
                peleas_ganadas = int(self.historial[peleador][0])
                self.ganador_record = peleador
        return self.ganador_record


# ejecucion
pelea1 = Pelea('El Kevin', 'El Braian')
pelea1.cargar_resultado(55, 50)
print(pelea1.obtener_ganador())


pelea2 = Pelea('El Kevin', 'El Lucho')
pelea2.cargar_resultado(55, 50)
print(pelea2.obtener_ganador())

pelea3 = Pelea('El Lucho', 'El Braian')
pelea3.cargar_resultado(55, 50)
print(pelea3.obtener_ganador(), '\n')

pelea4 = Pelea('El Lucho', 'El Braian')
pelea4.cargar_resultado(50, 50)
print(pelea4.obtener_ganador(), '\n')

historial = HistorialDePelea()
historial.cargar_pelea(pelea1)
historial.cargar_pelea(pelea2)
historial.cargar_pelea(pelea3)
historial.cargar_pelea(pelea4)
print(historial.historial)

print(historial.obtener_record())

