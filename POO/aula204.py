# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

        def get_ano_nascimento(self):
            return Pessoa.ano_atual - self.idade


dados = {'nome': 'Dezin', 'idade':29}
p1 = Pessoa(**dados)
print(p1.__dict__)

# print(p1.__dict__)
# print(vars(p1))
# p1.__dict__['outra'] = 'coisa'
# print(p1.outra)
# print(p1.__dict__)