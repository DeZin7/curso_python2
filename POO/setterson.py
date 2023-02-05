class Caneta:
    def __init__(self):
        self.nome = None

    @property
    def obter_nome(self):
        return self.nome

    @obter_nome.setter
    def obter_nome(self, nome):
        self.nome = nome

caneta = Caneta()
caneta.obter_nome = 'Caneta azul azul caneta'
print(caneta.nome)
