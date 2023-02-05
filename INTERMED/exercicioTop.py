import copy

from dados import produtos

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    {**produto, 'preco': round(produto['preco']*1.1, 2)}
    for produto in copy.deepcopy(produtos)
]

print(*novos_produtos, sep='\n')
print()

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'],
    reverse=True
)
print(*produtos_ordenados_nome, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto:produto['preco']
)

print(*produtos_ordenados_preco, sep='\n')
print()

print(*produtos, sep='\n')
