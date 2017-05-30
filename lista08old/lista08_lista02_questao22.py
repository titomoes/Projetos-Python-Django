# ----------------------------------------------------------------------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Edson de Lima Barros   1715310043
# Tiago Ferreira Aranha  1715310047
# Vitor Simôes Azevedo   1715310025
#
# 22. Faça um procedimento que receba, por parâmetro um vetor B(50) de reais e
# calcula o maior valor do vetor.
#
# A seguir, o procedimento deve dividir
# todos os elementos de B pelo maior encontrado.
# O vetor deve retornar alterado.


from lista08old.ipc import funcoes

vetor = funcoes.cria_vetor_numeros_decimais(50)

maior = funcoes.maior_valor_do_vetor(vetor)

print(funcoes.divide_todos_por_numero(vetor, maior))
