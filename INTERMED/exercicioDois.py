"""
Exercício
Crie uma função que encontra o primeiro duplicado considerando o segundo
número como a duplicação. Retorne a duplicação considerada.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1, 2, 3, ->3<-, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
        [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        [1, 4, 9, 8, ->9<-, 4, 8] (retorne 9)
    Se não encontrar duplicados na lista, retorne -1
"""
lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_duplicados(lista_de_inteiros):
    numeros_checados = set() #cria o set vazio
    numero_duplicado = -1    #até o momento não existe um número duplicado entao retorna -1

    for numero in lista_de_inteiros: #iterando a lista q recebemos
        if numero in numeros_checados: #conferindo se o numero da lista já foi passado alguma vez para o set
            numero_duplicado = numero  #caso o numero ja esteja no set, significa q ele já foi passado pra la e o set nao o armazenará novamente, logo temos o primeiro duplicado
            break #que é nossa condição de parada 

        numeros_checados.add(numero) #o set q vai armazenando os valores da lista após cada iteração

    return numero_duplicado #retorno



for lista in lista_de_listas_de_inteiros: #iterando a lista das listas pra obter uma lista
    print(lista, encontrar_duplicados(lista)) #aplicando a função

    #chama, felas!