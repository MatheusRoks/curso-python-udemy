class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.modelos = []

    def inserir_modelo(self, modelo, motor):
        self.modelos.append(Carro(modelo, motor))

    def exibir_modelos(self):
        for modelo in self.modelos:
            print(modelo.modelo, "-", modelo.motor.tipo)


class Carro:
    def __init__(self, modelo, motor):
        self.modelo = modelo
        self.motor = motor  # já recebe o motor no construtor

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor):
        self._motor = motor


class Motor:
    def __init__(self, tipo):
        self.tipo = tipo


# Teste
fabricante1 = Fabricante('Fiat')
motor1 = Motor('1.0')
motor2 = Motor('1.4')

fabricante1.inserir_modelo('Uno', motor1)
fabricante1.inserir_modelo('Palio', motor2)
fabricante1.exibir_modelos()
