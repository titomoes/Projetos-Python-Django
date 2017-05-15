# Criar um algoritmo que leia os elementos de uma matriz inteira 10 x 10 e escreva
# todos os elementos, exceto os elementos da diagonal principal

matriz = []
linhas = 10
colunas = 10
# gerando matriz
for i in range (linhas):
    lista=[]
    for j in range(colunas):
        lista.append(input())
    matriz.append(lista)

for i,n in enumerate(matriz):
    for j,m in enumerate(n):
        if i!=j:
            print(m, end=' ')