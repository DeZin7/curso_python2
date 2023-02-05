# Encapsulamento (modifcadores de acesso: public, prontected, private)
# Python NÃO tem modificadores de acesso 
# Mas podemos seguir as seguintes convenções
# (sem underline) = public
# significa que pode ser usado em qualquer lugar
# _(um underline) = protected
# significa que NÃO DEVE ser usado fora da classe ou suas subclasses
# __(dois underline, o famoso dunderline) = private
# "name mangling" (desfiguração de nomes) em Python
# __NomeClasse__nome_attr_ou_method
# significa que só deve ser usado na classe em que foi declarado

#pilares da POO = abstração, encapsulamento, herança e polimorfismo
# nesta aula falaremos sobre ENCAPSULAMENTO

class Foo:
    def __init__(self):
        self.pubclic = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é private'

    def metodo_publico(self):
        return 'método público'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_privates'

f = Foo()
# print(f.pubclic)
print(f.metodo_publico()) #pode ser acessado em qualquer lugar
print(f._metodo_protected()) #pode ser acessado na classe ou sua subclasse
print(f._Foo__metodo_private()) #private só pode ser usado na classe em que ele foi declarado 
