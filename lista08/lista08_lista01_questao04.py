# Faça um programa, com uma função que necessite de um argumento.
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo,
# e ‘N’, se seu argumento for zero ou negativo.

def positivo_negativo(arg):
    if arg > 0:
        res = "P"
    else:
        res = "N"
    return res

arg = int(input("Informe o número: "))

resposta = positivo_negativo(arg)

print(resposta)