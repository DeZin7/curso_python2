# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# adicionando notas em exceções (3.11.0)

class MeuError(Exception):
    ...

def levantar():
    raise MeuError('A mensagem do meu erro')


try:
    levantar()
except MeuError as error:
    print(error)