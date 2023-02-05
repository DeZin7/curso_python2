print('Bem vindo ao game de perguntas e respostas, lixão!')
print()
# contador_perguntas = 0
# contador_respostas_certas = 0



# print('Pergunta: Quanto é 2+2?')
# print()
# print('Opções:')
# for i in range(0,4):
#     print(f'{i}){i+1}')
# resposta1 = int(input('Escolha uma opção: '))
# if resposta1 == 3:
#     print("show! vc acertou man!")
#     contador_respostas_certas += 1
# else:
#     print("ops...errou...")

# print('Pergunta: Quanto é 5*5?')
# print()
# print('Opções:')

# print('0) 25')
# print('1) 55')
# print('2)')


# perguntas = [
#     {
#         'Pergunta': 'Quanto é 2+2?',
#         'Opções': ['1', '3', '4', '5'],
#         'Resposta': '4',
#     },
#     {
#         'Pergunta': 'Quanto é 5*5?',
#         'Opções': ['25', '55', '10', '51'],
#         'Resposta': '25',
#     },
#     {
#         'Pergunta': 'Quanto é 10/2?',
#         'Opções': ['4', '5', '2', '1'],
#         'Resposta': '5',
#     },
# ]

# print(perguntas[0]['Pergunta'])
# for i, opcao in enumerate(perguntas[0]['Opções']):
#     print(f'{i})', opcao)
# print()
# resposta1 = int(input('Escolha uma opção: '))
# contador_perguntas += 1
# if resposta1 == 2:
#     print('Show! Vc acertou man.')
#     contador_respostas_certas += 1
# else:
#     print('opss...vc errou...')
# print()

# print(perguntas[1]['Pergunta'])
# for i, opcao in enumerate(perguntas[1]['Opções']):
#     print(f'{i})', opcao)
# print()
# resposta2 = int(input('Escolha uma opção: '))
# contador_perguntas += 1
# if resposta2 == 0:
#     print('Show! Vc acertou man.')
#     contador_respostas_certas += 1
# else:
#     print('opss...vc errou...')
# print()

# print(perguntas[2]['Pergunta'])
# for i, opcao in enumerate(perguntas[2]['Opções']):
#     print(f'{i})', opcao)
# print()
# resposta3 = int(input('Escolha uma opção: '))
# contador_perguntas += 1
# if resposta3 == 1:
#     print('Show! Vc acertou man.')
#     contador_respostas_certas += 1
# else:
#     print('opss...vc errou...')

# print(f'vc respondeu {contador_respostas_certas} perguntas corretamente de um total de {contador_perguntas} perguntas!')

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})',opcao)
    print()

    escolha = input('Escolha uma opção: ')

