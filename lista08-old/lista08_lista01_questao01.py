# Faça um programa para imprimir:
#    1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n

from lista08a.ipc import funcoes

qtd = int(input("Informe a quantidade: "))

resposta  = funcoes.imprimir_questao1(qtd)

print(resposta)
