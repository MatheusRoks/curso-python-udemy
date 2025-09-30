class Escritor:
    def __init__(self, name):
        self.name = name
        self.ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrita:
    def __init__(self, ferrammenta):
        self.ferramenta = ferrammenta

    def escrever(self):
        return (f'Escrevendo com {self.ferramenta}')


escritor = Escritor('Matheus')
caneta = FerramentaDeEscrita('Caneta')
escritor.ferramenta = caneta

print(caneta.escrever())
