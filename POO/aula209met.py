# Métodos de classe + factories (fábricas que criam novos objetos)
# são métodos onde 'self' será 'cls', ou seja, 
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

# método de classe é o famoso @classmethod
# nada mais é do q ao invés de chamar a instância da classe (self), chama a classe em si (cls) como argumento
# e dessa forma, utilizando o decorator @classmethod, torna-se possível a criação de novos objetos (factories)

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod                # possibilita chamar o método sem usar o parâmetro self
    def metodo_de_classe(cls):  # ao invés disso o parâmetro torna-se a própria classe
        print('hey')

    @classmethod 
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', 50)

p1 = Pessoa('Joao', 34) 
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa.criar_sem_nome(25)
print(p3.nome, p3.idade)
print(p2.nome, p2.idade)
Pessoa.metodo_de_classe()