# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n

from lista08.ipc import funcoes

qtd = int(input("Informe a quantidade: "))

resposta = funcoes.imprimir_questao2(qtd)

print(resposta)
