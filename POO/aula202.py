# Escopo da classe e détodos da classe
# Escopo de classe é onde eu crio coisas, inclusive posso ter atributos de classes
# posso ter atributos de instâncias (dados de objetos) que usam a palavra self
# uma variável dentro de um método não pode ser chamada em outro método, afinal ela está no escopo de um único método
# a n ser q utilize self


class Animal:
    def __init__(self, nome):
        self.nome = nome

    variavel = 'valor'
    print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}...'

    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('Leão')
print(leao.nome)

print(leao.executar('maçã'))