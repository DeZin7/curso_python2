# Herança simples - Relação entre classes
# Associação - significa que usa
# Agregação - significa que tem
# Composição - significa que é dono de 
# Herança - significa que é um

# Herança vs Composição

# Classe principal (Pessoa)
# -> super class, base class, parent class
# Classes filhas (Cliente)
# -> sub class, child class, derived class

# Quando vc cria uma classe, vc está criando o seu próprio tipo

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Dezin', 'Top')
c2 = Aluno('Justine', 'Hunter')
# print(c1.nome, c1.sobrenome, c2.nome, c2.sobrenome)
c1.falar_nome_classe()
