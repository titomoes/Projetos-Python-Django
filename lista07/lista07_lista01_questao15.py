# Ler valores inteiros para a matriz A3x5. Gerar e imprimir a matriz (vetor) SL (soma das
# 3 linhas), onde cada elemento é a soma dos elementos de uma linha da matriz A. Faça
# o trecho que gera a matriz SL separado (laços de repetição) da entrada e da saída de
# dados.

matriz_A = []
vetor_SL = []
linhas = 3
colunas = 5


# gerando matriz
for i in range(linhas):
    lista_A = []
    for j in range(colunas):
        num = int(input())
        lista_A.append(num)
    matriz_A.append(lista_A)


for i, n in enumerate(matriz_A):
    soma = 0
    for j, m in enumerate(n):
        soma += matriz_A[i][j]

    vetor_SL.append(soma)

print(vetor_SL)