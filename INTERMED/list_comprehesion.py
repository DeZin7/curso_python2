#List comprehension é uma forma rápida para criar listas
#a partit de iteráveis.

# print(list(range(10)))

# lista = []
# for numero in range(10):
#     lista.append(numero)
# print(lista)

# lista =[numero*2 for numero in range(10)]
# print(lista)

#FILTRO DE DADOS: 

lista = [n for n in range (10) if n < 5]
print(lista)