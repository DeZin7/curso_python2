"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
   - Pessoa tem nome e idade (com getters) 
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC


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


# andre = Pessoa()
# andre.nome_pessoa = 'André'
# andre.idade_pessoa = 25
# print(andre.nome)
# print(andre.idade)

class Conta(ABC):
    def __init__(self, agencia, numeroconta, saldo):
        self.agencia = agencia
        self.numeroconta = numeroconta
        self.saldo = saldo

    def deposito(self, valor_deposito):
        self.saldo += valor_deposito
        return self.saldo

    

    

class Cliente(Pessoa):
    ...