# Herança Mútipla - Python Orientado a Objetos
# Quer dizer que no python uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> mamifero -> humano -> pessoa -> cliente
# herança múltipla e mixins
# log -> Filelog
# animal -> mamifero -> humano -> pessoa -> cliente
# cliente(Pessoa, Filelog)

# python 3 usa C3 superclass linearization para gerar o mro (method resolution order - ordem de resolução do método)
# não precisa estudar isso agora

# para saber a ordem de chamada dos métodos
# use o método de classe Classe.mro()
# ou o atributo __mro__ (Dunder)

class A:
    ...

    def quem_sou(self):
        print('A')

class B(A):
    ...

    # def quem_sou(self):
    #     print('B')

class C(A):
    ...

    def quem_sou(self):
        print('C')

class D(B,C):
    ...

    # def quem_sou(self):
    #     print('D')

d =D()
d.quem_sou()
print(D.__mro__)