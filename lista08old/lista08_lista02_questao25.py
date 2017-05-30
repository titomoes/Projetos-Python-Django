#25. Faça uma função que recebe, por parâmetro, uma matriz A(6,6) e retorna a soma dos elementos da sua diagonal principal e da sua diagonal secundária.


from lista08.ipc import matriz

matriz1 = matriz.cria_matriz(6, 6)

soma1=matriz.media_diagonal_principal(matriz1)

valor = matriz.soma_diagonais(matriz1)
print(matriz1)
print(valor)
