# 26. Faça uma função que recebe, por parâmetro, uma matriz A(7,6)
# e retorna a soma dos elementos da linha 5 e da coluna 3.


from lista08.ipc import matriz

matriz1 = matriz.cria_matriz(7, 6)

soma = matriz.soma_linha5_coluna3(matriz1)
matriz.imprime_matriz(matriz1)
print(soma)
