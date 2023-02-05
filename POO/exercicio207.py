# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.


import json

CAMINHO_ARQUIVO = 'exercicio207.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

pessoa1 = Pessoa('Dezin', 29)
pessoa2 = Pessoa('Justine', 29)
pessoa3 = Pessoa('Nyla', 0)
bd = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]



with open(CAMINHO_ARQUIVO, 'w') as arquivo:
    json.dump(bd, arquivo, indent=2, ensure_ascii=False)

