# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#         @property
#         def cor(self):
#             return self.cor_tinta


# caneta1 = Caneta('Azul')
# print(caneta1.cor)


class Pincel:
    def __init__(self, cor):
        self._cor_tinta = cor

    @property
    def cor(self):
        return self._cor_tinta

    @cor.setter
    def cor(self, nova_cor):
        self._cor_tinta = nova_cor


Pincel.cor = 'Vermelho'
print(Pincel.cor)
