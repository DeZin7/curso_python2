#len - quantas chaves
#keys - iteravel com as chaves
#values - iteravel com os valores
#items - iteravel com chaves e valores
#setdefault - adiciona valor se a chave não existe
#copy - retorna uma copia rasa (shallow copy) --> cópia rasa
#pop - apaga um item com a chave especificada (del)
#popitem - apaga o ultimo item adicionado
#update - atualiza um dicionário com outro

pessoa = {
    'nome': 'Marcus Andre',
    'sobrenome': 'Carneiro',
}

# print(len(pessoa))
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())

# for value in pessoa.values():
#     print(value)

# for key, value in pessoa.items():
#     print(key, value)

# pessoa.setdefault('idade', 200)
# print(pessoa['idade'])

# print(pessoa.get('nome', 'Dezin'))

pessoa.update({
    'idade': 200,
    'profissao': 'dev',
})
print(pessoa)