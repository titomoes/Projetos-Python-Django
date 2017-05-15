# Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e imprima o
# produto dos elementos que estão abaixo da diagonal principal.

matriz = []
linhas = 10
colunas = 10
produto = 1
# gerando matriz
for i in range (linhas):
    lista=[]
    for j in range(colunas):
        lista.append(input())
    matriz.append(lista)

for i,n in enumerate(matriz):
    for j,m in enumerate(n):
        if j<i:
            produto *= int(m)

print(produto)