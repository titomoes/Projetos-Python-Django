# . Sudoku	é	um	quebra‐cabeça,	cujo	objetivo do	jogo é	preencher	os	números	de
# 1	 a	 9	 em	 cada	 uma	 das	 células	 vazias	 numa	 grade	 de	 9×9,	 constituída	 por	 3×3
# subgrades	chamadas	 regiões.	Cada	coluna,	linha	e	 região	só	pode	 ter	um	número
# de	cada	um	dos	números	de	1	a	9.	Exemplo	de	um	jogo:

import random

tabuleiro = []
linhas = 9
colunas = 9
# gerando matriz
for i in range(linhas):
    lista = []

    for j in range(colunas):
        r = random.randint(1, 2)
        if r == 2:
            lista.append("[%s]" % (random.randrange(1, 9)))
        else:
            lista.append("[ ]")
    tabuleiro.append(lista)

for i in tabuleiro:
    for j in i:
        print(j, end=' ')
    print()

for i, m in enumerate(tabuleiro):
    for n in m:
        igual = 0
        if m[i] != "[  ]" and n != "[  ]":
            if m[i] == n:
                igual += 1
    if igual > 0:
        print("Jogo está incorreto")
        correto = 0
        break

