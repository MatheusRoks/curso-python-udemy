

class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self._fabricante = fabricante


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo


fusca = Carro('Fusca')
fusca.fabricante = Fabricante('Volkswagen')
fusca.motor = Motor('1.6')
print(fusca.modelo, fusca.fabricante.nome, fusca.motor.tipo)
