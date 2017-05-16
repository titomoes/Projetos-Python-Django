# Ler uma matriz 4x5 de inteiros, calcular e imprimir a soma de todos os seus
# elementos.

matriz_A = []
linhas = 4
colunas = 5
soma = 0

# gerando matriz
for i in range(linhas):
    lista_A = []
    for j in range(colunas):
        num = int(input())
        lista_A.append(num)
        soma += num
    matriz_A.append(lista_A)

print(soma)
