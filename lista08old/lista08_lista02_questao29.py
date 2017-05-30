# 29. Faça um procedimento que receba, por parâmetro, duas matrizes A(4,6) e B(6,4)
# e retorna uma matriz C, também por parâmetro,
# que seja o produto matricial de M por N.



from lista08.ipc import matriz

matrizA = matriz.cria_matriz(2, 2)
matrizB = matriz.cria_matriz(2, 2)


matrizC = matriz.cria_matriz_zerada(2,2)

matriz.imprime_matriz(matrizA)
matriz.imprime_matriz(matrizB)
# lista 2 questão 29
def produto_matriz(matriz1, matriz2):


    for i in range(2):
        for j in range(2):
            print("c", i, j, " = ", "a", i, 0, " - ", "b", 0, j, " - ", "a", i, 1, " - ", "b", 1, j)
            matrizC[i][j] = matriz1[i][0] * matriz2[0][j] + matriz1[i][1] * matriz2[1][j]
    return matrizC


matriz_final = produto_matriz(matrizA, matrizB)
matriz.imprime_matriz(matriz_final)
