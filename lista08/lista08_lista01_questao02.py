# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n

def imprimir(n):
    res = ""
    c = 1
    for i in range(n+1):
        #res += str(i + 1) + "\n"
        for j in range(i):
            res += str(j+1) + " "
        res += "\n"
    return res


qtd = int(input("Informe a quantidade: "))

resposta = imprimir(qtd)

print(resposta)
