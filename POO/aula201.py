# Entendendo self em classes Python
# self é uma convenção. self sempre deve ser o primeiro parâmetro
# a classe funciona como um molde e ela não possui dados (atributos) quando é criada 
# a instância (objeto) da classe possui os dados
# uma classe pode gerar vária instâncias (objeto)
# na classe o self é a própria instância, ou seja, o self é o próprio objeto


class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')



fusca = Carro('Fusca')
fusca.acelerar()
Carro.acelerar(fusca)

celta = Carro('Celtinha')
celta.acelerar()
Carro.acelerar(celta)