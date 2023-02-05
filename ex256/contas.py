import abc


class Conta(abc.ABC):
    def __init__(self, agencia, numeroconta, saldo=0):
        self.agencia = agencia
        self.numeroconta = numeroconta
        self.saldo = saldo
    
    @abc.abstractmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.detalhes(f'(DEPÓSITO {valor_deposito})')
        return self.saldo

    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f} {msg}')
        print('--')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numeroconta!r}, {self.saldo!r})'
        return f'{class_name}{attrs}'

class ContaPoupanca(Conta):
    def sacar(self,valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print('Não foi possível sacar o valor desejado')
        self.detalhes(f'(SAQUE NEGADO: {valor})')

# if __name__ == '__main__': #para executar apenas neste módulo, sem utilizar o teste no módulo q importar este módulo 
#     cp1 = ContaPoupanca('000', '222', 0)
#     cp1.sacar(1)
#     cp1.depositar(1)
#     cp1.sacar(1)
#     cp1.sacar(1)

class ContaCorrente(Conta):
    def __init__(self, agencia, numeroconta, saldo=0, limite=0):
        super().__init__(agencia, numeroconta, saldo=0) #passando as coisas q a superclasse precisa. Necessário fazer devido a criação de um novo parâmetro
        self.limite = limite


    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_pos_saque >= limite_maximo:

            self.saldo -= valor
            self.detalhes(f'(SAQUE {valor})')
            return self.saldo
        
        print(f'NÃO FOI POSSÍVEL SACAR O VALOR DESEJADO')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'(SAQUE NEGADO {valor})')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.numeroconta!r}, {self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'

if __name__ == '__main__': #para executar apenas neste módulo, sem utilizar o teste no módulo q importar este módulo 
    cc1 = ContaCorrente('000', '222', 0, 100)
    cc1.sacar(1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(98)
    cc1.sacar(5)