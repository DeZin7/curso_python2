# super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class 

class MinhaString(str): #str ta funcionando como minha superclass
    def upper(self):
        print('CHAMOU UPPER') #ADICIONEI FUNCIONALIDADE AO MÉTODO Q JÁ EXISTIA NA SUPER CLASS
        return super().upper() #PORÉM UTILIZANDO super().upper() EU NÃO SOBRESCREVI A CLASSE, PRESERVEI AS MESMAS FUNCIONALIDADES
                                # E ADICIONEI O PRINT


string = MinhaString('dezin')
print(string.upper())
