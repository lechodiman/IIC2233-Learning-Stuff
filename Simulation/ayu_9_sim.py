import random
from collections import deque


class Jugador:

    def __init__(self, id):
        self.id = id
        self.habilidad = random.uniform(1, 10)
        self.jugados = 0

    def win_vs(self, oponent):
        p = random.choice([True, False])
        if self.habilidad > oponent.habilidad and p:
            return True
        else:
            return False

    @property
    def retirarse(self):
        if self.jugados > random.uniform(1, 10):
            return True
        else:
            return False

    def __repr__(self):
        return "Jugador {}".format(self.id)


class Simulacion:

    def __init__(self, jugadores=3, tiempo_max=70):
        self.cola = deque()
        self.jugando = deque()
        self.lista_eventos = list()
        for i in range(jugadores):
            self.cola.append(Jugador(i))
        self.id = i + 1
        self.tiempo_max = tiempo_max

    def ordenar_lista(self):
        self.lista_eventos.sort(key=lambda x: x[0])

    def tiempo_llegada(self, tiempo):
        self.lista_eventos.append((tiempo + random.expovariate(1 / 15), 'llegada'))

    def tiempo_partido(self, tiempo):
        self.lista_eventos.append((tiempo + random.uniform(4, 5), 'fin partido'))

    def llenar_mesa(self, tiempo):
        if len(self.jugando) < 2:
            if len(self.jugando) == 0:
                if len(self.cola) >= 1:
                    self.jugando.append(self.cola.popleft())
            if len(self.jugando) == 1:
                if len(self.cola) >= 1:
                    self.jugando.append(self.cola.popleft())
            if len(self.jugando) == 2:
                print("[{}] Comienza partido entre {}, {}".format(tiempo, *self.jugando))
                self.tiempo_partido(tiempo)

    def llegada_personas(self, tiempo):
        self.tiempo_llegada(tiempo)
        p = Jugador(self.id)
        self.id += 1
        self.cola.append(p)
        print('[{}] LLegó la persona {}'.format(tiempo, p))

    def fin_partido(self, tiempo):
        j1 = self.jugando.popleft()
        j2 = self.jugando.popleft()
        if j1.win_vs(j2):
            if not j2.retirarse:
                self.cola.append(j2)
            self.jugando.append(j1)
        else:
            if not j1.retirarse:
                self.cola.append(j1)
            self.jugando.append(j2)
        print('[{}] Termino el partido entre {} y {}'.format(tiempo, j1, j2))
        self.llenar_mesa(tiempo)

    def run(self):
        tiempo = 0
        self.tiempo_llegada(tiempo)

        while len(self.lista_eventos) != 0:
            tiempo, evento = self.lista_eventos[0]
            self.lista_eventos = self.lista_eventos[1:]
            if tiempo > self.tiempo_max:
                tiempo = self.tiempo_max
                break

            self.llenar_mesa(tiempo)

            if evento == 'llegada':
                self.llegada_personas(tiempo)
            elif evento == 'fin partido':
                self.fin_partido(tiempo)

            self.ordenar_lista()

s = Simulacion()
s.run()
