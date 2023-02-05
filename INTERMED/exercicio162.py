# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def interna(y):
        return funcao(x,y)
    return interna


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

print(soma_com_cinco(2))
print(multiplica_por_dez(3))

# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}'
#     return saudar

# falar_bom_dia = criar_saudacao('bom dia')

# s1 = falar_bom_dia('Clara')
# print(s1)