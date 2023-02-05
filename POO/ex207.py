import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


pessoa1 = Pessoa('Joao', 25)
pessoa2 = Pessoa('Maria', 90)

dados = [pessoa1.__dict__, pessoa2.__dict__]

CAMINHO = 'ex207_dois'

with open(CAMINHO, 'w') as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=2)