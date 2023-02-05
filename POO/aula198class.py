#class - Classes são moldes para criar novos objetos
#As classes geram novos objetos (instâncias) que
#podem ter seus próprios atributos e métodos. Os
#objetos criados por sua classe podem usar seus dados
#internos para realizar várias ações. Por convenção
#usamos PascalCase para nomes de classes. 


#INSTÂNCIA = OBJETO CRIADO DENTRO DA CLASSE
#MÉTODO = FUNÇÃO CRIADA DENTRO DA CLASSE
#ATRIBUTOS = DADOS DENTRO DA CLASSE

# string = 'Dezin'
# print(string.upper())
# print(isinstance(string,str))

class Pessoa:
    ...

p1 = Pessoa()
p1.nome = 'Dezin'
p1.sobrenome = 'Carneiro'

p2 = Pessoa()
p2.nome = 'Justine'
p2.sobrenome = 'Hunter'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)

#sendo assim p1 e p2 são objetos diferentes com atributos diferentes 
#não se chama um atributo utilizando () no final, afinal de contas o
#compilador tentará invocar um método, por exemplo, seria completamente
#errado colocar p1.nome()