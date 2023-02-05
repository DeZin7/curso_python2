def criar_funcao(func):
    def interna(y):
        print('show de bola, vc foi decorado!')
        return 5 + y 
    return interna

@criar_funcao
def soma_mais_cinco(y):
    return

print(soma_mais_cinco(2))
print(soma_mais_cinco(10))
print()


def decoradora(func):
    
    def interna(y):
        print('bacana, agora tu foi decorado de novo!')
        return 10*y
    return interna

@decoradora
def multiplicar_por_dez(y):
    return

print(multiplicar_por_dez(2))
print(multiplicar_por_dez(5))
