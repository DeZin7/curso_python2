# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes derivadas de uma superclasse 
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de Liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

#Sobrecarga de métodos (overload)
#Sobreposição de métodos (override)


from abc import ABC, abstractmethod


class Notificacao(ABC):

    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self): ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS: enviando - ', self.mensagem)


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar

    if notificacao_enviada:
        print('Notificação enviada')
    else: 
        print('Notificação não enviada')




notificacao_email = NotificacaoEmail('testando email')
notificar(notificacao_email)


notificacao_sms = NotificacaoSMS('testando sms')
notificar(notificacao_sms)
# n = NotificacaoEmail('testando notificacao')
# n.enviar()