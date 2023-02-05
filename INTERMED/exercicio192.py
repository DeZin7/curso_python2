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

tarefas = []
tarefas_refazer = []

def listar(tarefas):
    print()
    if len(tarefas) == 0:
        print('Nenhuma tarefa para listar, irmão.')
        return 

    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()

def desfazer(tarefa, tarefas_refazer):
    print()
    if len(tarefas) == 0:
        print('Nada a desfazer, irmão.')
        return 

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista.')
    tarefas_refazer.append(tarefa)
    print()

def refazer(tarefa, tarefas):
    print()
    if len(tarefas) == 0:
        print('Nada a refazer, irmão')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()

def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nao digitou nada, irmao')
        return
    print(f'{tarefa} adicionada na lista, irmão')
    tarefas.append(tarefa)
    print()

while True:
    print('Comando: listar, desfazer, refazer')
    tarefa = input(str('Digite uma tarefa ou comando: '))

    if tarefa == 'listar':
        listar(tarefas)
        continue

    elif tarefa == 'desfazer':
        desfazer(tarefa, tarefas_refazer)
        listar(tarefas)
        continue

    elif tarefa == 'refazer':
        refazer(tarefa, tarefas_refazer)
        listar(tarefas)
        continue
    
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue






