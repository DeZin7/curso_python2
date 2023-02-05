# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e 
# retornar o novo objeto. Por isso new recebe cls.
# __new__ deve retornar o novo objeto!
# __init__ é o método resposável por inicializar a instância
# e, portanto __init__ recebe self
# __init__ não deve retornar nada (None)
# object é a super classe de uma classe

class A:
    def __new__(cls):
        print('Antes de criar a instância')
        instancia = super().__new__(cls)
        print('Depois')
        return instancia

    def __init__(self):
        print('Sou o init')

    def __repr__(self):
        return 'A()'

a = A()


class B:
    def __init__(self) -> None:
        pass
