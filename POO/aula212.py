# @property é um getter no modo pythônico
# getter é um método para obter um atributo
# modo pythônico - modo do Python de fazer coisas
# é um método que se comporta como um atributo 
# Geralmente é utilizado nas seguintes situações:
# - como getter
# - para evitar quebra de código de cliente
# - para habilitar setter
# - para executar ações ao obter um atributo 

class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

    @property
    def cor_tampa(self):
        return 123456


caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.cor_tampa)