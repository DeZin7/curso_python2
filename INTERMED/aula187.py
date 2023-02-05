import os

caminho_arquivo = 'aula187.txt'

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n' , 'Linha 4\n')
    )

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

os.unlink(caminho_arquivo)