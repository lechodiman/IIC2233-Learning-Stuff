from random import expovariate, choice, randrange, random
from collections import deque

tiempo_llegada_cliente = round(expovariate(1 / 20) + 0.5)
tiempo_atencion_1 = round(expovariate(1 / 50) + 0.5)
tiempo_atencion_2 = round(expovariate(1 / 50) + 0.5)

print(tiempo_llegada_cliente)
print(tiempo_atencion_1)
print(tiempo_atencion_2)


class Vehiculo:
    # Esta clase modela los vehiculos que llegan al taller

    def __init__(self, vehiculos):

        # Cuando se crea un nuevo vehículo se escoge aleatoriamente el tipo de vehículo
        # entrante y su tiempo promedio de atención

        self.tipo_vehiculo = choice(list(vehiculos))
        self._tiempo_revision = round(expovariate(vehiculos[self.tipo_vehiculo]) + 0.5)

    @property
    def tiempo_revision(self):
        return self._tiempo_revision

    @tiempo_revision.setter
    def tiempo_revision(self, valor):
        self._tiempo_revision = valor


class Taller:
    # Esta clase modela la linea de revision en el taller
    def __init__(self):
        self.tarea_actual = None
        self.tiempo_revision = 0

    @property
    def ocupado(self):
        return self.tarea_actual != None

    def proximo_auto(self, vehiculo):
        self.tarea_actual = vehiculo
        self.tiempo_revision = vehiculo.tiempo_revision
        print('[PLANTA] Atendiendo {0} con un tiempo promedio de {1} min'.format(
            self.tarea_actual.tipo_vehiculo, self.tiempo_revision))

    def tick(self):
        if self.tarea_actual != None:
            self.tiempo_revision -= 1
            if self.tiempo_revision <= 0:
                print('[Planta] termina revision de {}'.format(self.tarea_actual.tipo_vehiculo))
                self.tarea_actual = None


def llega_nuevo_auto():
    # Esta funcion modela si llega o no un auto nuevo a la cola.
    # Se muestrea de una distribución de probabilidad uniforme. El método retorna
    # True si el valor entregado por la función random es mayor a un valor dado.

    return random() >= 0.8


def revision_tecnica(max_tiempo, vehiculos):
    # Esta funcion maneja el proceso o servicio de revision en el taller

    # se crea una planta de revisión
    planta = Taller()

    # cola de revision vacia
    cola_revision = deque()

    # tiempos de espera
    tiempo_espera = []

    # Se define el ciclo de simulación al máximo tiempo en minutos difinido,
    # donde en cada instante t se evelúa si llega un nuevo vehículo
    # a la cola de revisión

    for t in range(max_tiempo):

        if llega_nuevo_auto():
            cola_revision.append(Vehiculo(vehiculos))
            print('[COLA] llega {} en tiempo de simulacion t={} min. Hay {} vehiculos en la cola.'.format(
                cola_revision[-1].tipo_vehiculo, t, len(cola_revision)))

        if (not planta.ocupado) and (len(cola_revision) > 0):

            # se extrae el proximo auto en la cola de atención

            ac_auto = cola_revision.popleft()
            tiempo_espera.append(ac_auto.tiempo_revision)
            planta.proximo_auto(ac_auto)

        # descuenta un tick de tiempo al auto en espera
        planta.tick()

    tiempo_promedio = sum(tiempo_espera) / len(tiempo_espera)
    tiempo_total = sum(tiempo_espera)

    print()
    print('Estadísticas:')
    print('Tiempo promedio de espera {0:6.2f} min.'.format(tiempo_promedio))
    print('Tiempo total de atención de la planta fue de {0:6.2f} min'.format(sum(tiempo_espera)))
    print('Total de vehículos atendidos: {0}'.format(len(tiempo_espera)))


'''
vehiculos = {'moto': 1.0 / 8, 'auto': 1.0 / 15, 'camioneta': 1.0 / 20}
maximo_tiempo = 40

revision_tecnica(maximo_tiempo, vehiculos)
'''
