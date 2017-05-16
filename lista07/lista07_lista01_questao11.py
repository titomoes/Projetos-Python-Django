# Entrar com valores para uma matriz A3x4. Gerar e imprimir uma matriz B que é o
# triplo da matriz A

matriz_A = []
matriz_B = []
linhas = 3
colunas = 4

# gerando matriz
for i in range (linhas):
    lista_A = []
    lista_B = []
    for j in range(colunas):
        num = int(input())
        lista_A.append(num)
        lista_B.append(num * 3)
    matriz_A.append(lista_A)
    matriz_B.append(lista_B)

print(matriz_A)
print(matriz_B)