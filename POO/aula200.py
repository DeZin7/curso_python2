# Métodos em instâncias de classes Python. instância é o objeto
# um método nada mais é do que uma função que está dentro de uma classe
# e sempre que essa função for para um objeto, nós usaremos a palavra self
# self é o mesmo que o objeto fora da classe

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')



fusca = Carro('Fusca')
fusca.acelerar()

celta = Carro('Celtinha')
celta.acelerar()