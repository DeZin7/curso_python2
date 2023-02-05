# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

def listar(tarefas):
    print()
    if len(tarefas) == 0:
        print('Não há nada para listar.')
        print()
        return
    print('\tTAREFAS:')
    for tarefa in tarefas:
        print(f'{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if len(tarefas) == 0:
        print('Não há nada para desfazer.')
        print()
        return
    tarefa = tarefas.pop()
    print(f'{tarefa} removida com sucesso.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if len(tarefas) == 0:
        print('Não há nada para refazer.')
        print()
        return
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa} refeita com sucesso.')
    tarefas = tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
    tarefas.append(tarefa)
    print(f'{tarefa} adicionada com sucesso.')
    print()




import json
import os


def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open('caminho_arquivo', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe.')
        salvar(tarefas, caminho_arquivo)
    return dados


def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados

CAMINHO_ARQUIVO = 'dados192.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer')
    tarefa = input('Digite uma tarefa ou um comando: ')

    if tarefa == 'listar':
        listar(tarefas)
    

    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)

    
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
    
    elif tarefa == 'clear':
        os.system('clear')
    
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)

    salvar(tarefas, CAMINHO_ARQUIVO)


        