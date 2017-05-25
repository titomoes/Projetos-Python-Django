# Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n

def imprimir(n):
    res = ""
    c = 1
    for i in range(n):
        res += c * (str(i + 1) + " ") + "\n"
        c += 1
    return res

qtd = int(input("Informe a quantidade: "))

resposta  = imprimir(qtd)

print(resposta)
