from collections import deque
from random import uniform


class Cliente:
    pass


class Caja:
    def __init__(self, t):
        self.cola = deque()
        self.termino = 2 * t


class Banco:

    def __init__(self, t):
        self.cajas = [Caja(t), Caja(t)]


class Simulacion:

    def __init__(self, tiempo_maximo, llegada, salida):
        self.tiempo_maximo_sim = tiempo_maximo
        self.tiempo_simulacion = 0
        self.tiempo_proximo_cliente = uniform(1, llegada)
        self.banco = Banco(tiempo_maximo)
        self.salida = salida
        self.llegada = llegada

    def sale_primero(self, si, no):
        cola = self.banco.cajas[si].cola
        print('[inicio] sale caja', si, len(self.banco.cajas[si].cola), len(
            self.banco.cajas[no].cola))
        if len(self.banco.cajas[si].cola) > 0:
            cola.popleft()
        if len(self.banco.cajas[no].cola) > len(self.banco.cajas[si].cola) + 1 >= 0:
            print('cambio a 0')
            self.banco.cajas[si].cola.append(self.banco.cajas[no].cola.popleft())
        if len(self.banco.cajas[si].cola) == 0:
            self.banco.cajas[si].termino = 2 * self.tiempo_maximo_sim
        else:
            self.banco.cajas[si].termino = self.tiempo_simulacion + uniform(1, self.salida)
        print("[final] sale caja", si, len(self.banco.cajas[si].cola), len(
            self.banco.cajas[no].cola))

    def llega_primero(self, primero):
        print('llega cliente', primero)
        self.tiempo_proximo_cliente = self.tiempo_simulacion + \
            uniform(1, self.llegada)

        if len(self.banco.cajas[0].cola) <= len(self.banco.cajas[1].cola):
            if len(self.banco.cajas[0].cola) == 0:
                self.banco.cajas[0].termino = self.tiempo_simulacion + \
                    uniform(1, self.salida)
            self.banco.cajas[0].cola.append(Cliente())
        else:
            if len(self.banco.cajas[1].cola) == 0:
                self.banco.cajas[
                    1].termino = self.tiempo_simulacion + uniform(1, self.salida)
            self.banco.cajas[1].cola.append(Cliente())
        print('colas', len(self.banco.cajas[0].cola), len(
            self.banco.cajas[1].cola))

    def run(self):

        while True:
            primero = min(self.banco.cajas[0].termino, self.banco.cajas[
                          1].termino, self.tiempo_proximo_cliente)
            if primero >= self.tiempo_maximo_sim:
                break

            self.tiempo_simulacion = primero

            if self.tiempo_proximo_cliente == primero:
                self.llega_primero(primero)
            else:
                if self.banco.cajas[0].termino == primero:
                    self.sale_primero(0, 1)
                else:
                    self.sale_primero(1, 0)


s = Simulacion(tiempo_maximo=80, llegada=3, salida=10)
s.run()
