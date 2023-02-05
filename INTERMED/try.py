#try, except, else e finally

try:
    print('ABRIR ARQUIVO')
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU POR ZERO')
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError', 'ImportError')
else:
    print('NÃO DEU ERRO')
finally:                        #finally sempre será executado
    print('FECHAR ARQUIVO')


#try pode ser usado somente com o finally e aí não tratamos excessão 
#try pode ser usado com except e aí tratamos a excessão 
#