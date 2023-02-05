lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

# def ordena(item):
#     return item['nome']

lista.sort(key=lambda item: item['nome']) #função lambda ta fazendo a msm coisa q a função acima, lambda representa o 'def', 'item' é o parametro
print(lista)                              # item['nome'] é o retorno da funçãos