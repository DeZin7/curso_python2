# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

# o propperty chama uma função q retorna um atributo
# o setter chama a função com mesmo nome recebendo um atributo

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante  = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome

uno = Carro('uno')
motor1000 = Motor('1.0 turbo')
fiat = Fabricante('Fiat')
uno.motor = motor1000
uno.fabricante = fiat
print(uno.nome, uno.fabricante.nome, uno.motor.nome)

gol = Carro('gol bola prata')
volks = Fabricante('Volkswagen')
gol.motor = motor1000
gol.fabricante = volks
print(gol.nome, gol.fabricante.nome, gol.motor.nome)