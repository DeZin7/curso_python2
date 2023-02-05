# s1 = set('DEZIN')
# print(s1)

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #união entre conjuntos
s3 = s1 & s2 #intersecção entre conjuntos
s3 = s1 - s2 #diferença entre conjuntos 
s3 = s1 ^ s2 #diferença simétrica entre conjuntos. Itens que não estão em ambos os conjuntos
print(s3)