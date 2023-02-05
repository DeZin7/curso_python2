#introdução ao método __init__
#__init__ inicializa os atributos da classe, recebe self como primeiro parâmetro 
#a instância da classe está em self. Lembrando que INSTÂNCIA = OBJETO DA CLASSE

class Pessoa:
    def __init__(self, nome, sobrenome):     #o __init__ simplesmente inicia os atributos da classe
        self.nome = nome                     #criando um atributo na classe. Lembrando q atributos são dados do objeto criado na classe (instância)
        self.sobrenome = sobrenome

p1 = Pessoa('Dezin', 'Carneiro')
# p1.nome = 'Dezin'
# p1.sobrenome = 'Carneiro'

p2 = Pessoa('Justine', 'Hunter')
# p2.nome = 'Justine'
# p2.sobrenome = 'Hunter'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)