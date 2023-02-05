# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos estão 
# ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição.
# GERALMENTE TEMO UMA ASSOCIAÇÃO QUANDO UM OBJETO TEM UM ATRIBUTO QUE REFERENCIA OUTRO OBJETO
# A associação não especifica como um objeto controla o ciclo de vida de outro objeto

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerrramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'

escritor = Escritor('Dezin')
caneta = FerrramentaDeEscrever('caneta bic')
escritor.ferramenta = caneta #associação sendo feita

print(caneta.escrever())
print(escritor.ferramenta.escrever())
    