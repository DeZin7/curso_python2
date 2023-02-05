# pessoas = {
#     'nome': 'dezin seven',
#     'sobrenome': 'top',
# }
# # print(pessoas, type(pessoas))
# for chave in pessoas:
#     print(chave, pessoas[chave])

pessoa = {}

chave = 'nome'

pessoa[chave] = "Dezin7 Delicia"
pessoa['sobrenome'] = 'vinte'
lista = []

# del pessoa['sobrenome']

if pessoa.get('sobrenome') is None:
    print("Não existe, felas.")
else:
    print("Existe felas.")

print('este modulo se chama', __name__)
# print(pessoa)
# print(pessoa[chave])

