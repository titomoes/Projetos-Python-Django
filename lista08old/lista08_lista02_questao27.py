# 27. Faça uma função que recebe, por parâmetro, uma matriz A(6,6)
# e retorna o menor elemento da sua diagonal secundária.

from lista08.ipc import matriz, vetor

matriz1 = matriz.cria_matriz(6, 6)

diagonal_secundaria = matriz.diagonal_secundaria(matriz1)

menor_valor = vetor.menor_valor_do_vetor(diagonal_secundaria)

matriz.imprime_matriz(matriz1)

print(diagonal_secundaria)

print(menor_valor)