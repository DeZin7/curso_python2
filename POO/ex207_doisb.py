import json

from ex207 import CAMINHO, Pessoa

with open(CAMINHO, 'r') as arquivo:
    data = json.load(arquivo)
    p1 = Pessoa(**data[0])
    print(p1.nome, p1.idade)