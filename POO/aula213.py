# @property + @setter - getter e setter no pythonico
# como getter
# para evitar quebrar codigo do cliente
# para habilitar setter
# para executar ações ao obter um atributo

# método não salva valor!!! método executa ações!!!
# self._cor , se vc ver um atributo com um underline (ou dois) significa q ele n deve ser usado fora da classe (convenção)

# o setter é um método que recebe o self (pois precisa ter acesso a coisas do objeto da classe) e também precisa receber um parâmetro
# o setter pode ser utilizado para restringir as coisas, como mostra o exemplo abaixo restringindo a cor da caneta

class Caneta:
    def __init__(self, cor):
        self._cor= cor

    @property
    def cor(self):
        print('PROPERTY')
        return self._cor

    @cor.setter
    def cor(self, valor):
        if valor == 'Rosa':
            raise ValueError('Não aceito essa cor')
        self._cor = valor


caneta = Caneta('AZUL')
caneta.cor = 'Pink'
print(caneta.cor)
# getter -> obter valor
