# def recursiva(inicio=0, fim=10): 
#     if inicio >= 10:
#         return fim

#     inicio +=1
#     return recursiva(inicio, fim)

# print(recursiva())

# def factorial(n):
#     if n <= 1:
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))

# 0, 1, 1, 2, 3, 5,...
#receber um numero
#o numero é a soma dos dois antecessores

first = 0
second = 1
print(first)
print(second)
for numero in range(1,9):
    third = first + second
    print(third)
    first, second = second, third
    




