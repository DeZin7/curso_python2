import contas


class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome_pessoa(self):
        return self._nome

    @nome_pessoa.setter
    def nome_pessoa(self, nome):
        self._nome = nome

    @property
    def idade_pessoa(self):
        return self._idade

    @nome_pessoa.setter
    def idade_pessoa(self, idade):
        self._idade = idade

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'{self.nome!r}, {self.idade!r}'
        return f'{class_name}({attrs})'

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None

if __name__ == '__main__':
    c1 = Cliente('Dezin', 30)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)
    c2 = Cliente('Justine', 35)
    c2.conta = contas.ContaCorrente(112, 223, 1, 1)
    print(c2)
    print(c2.conta)