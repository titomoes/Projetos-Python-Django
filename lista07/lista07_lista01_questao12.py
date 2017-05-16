# Entrar com valores inteiros para um matriz A4x4 e para uma matriz B4x4. Gerar e
# imprimir a SOMA (A+B).

matriz_A = []
matriz_B = []
matriz_C = []
linhas = 4
colunas = 4

# gerando matriz
for i in range(linhas):
    lista = []
    for j in range(colunas):
        num = int(input())
        lista.append(num)
    matriz_A.append(lista)

print("=======")

# gerando matriz
for i in range(linhas):
    lista = []
    for j in range(colunas):
        num = int(input())
        lista.append(num)
    matriz_B.append(lista)

for i, n in enumerate(matriz_A):
    lista = []
    for j, m in enumerate(n):
        lista.append(matriz_A[i][j] + matriz_B[i][j])

    matriz_C.append(lista)

print(matriz_C)
