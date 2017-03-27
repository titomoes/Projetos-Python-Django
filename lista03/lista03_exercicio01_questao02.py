# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
# ----------------------------------------------------------
n1 =int(input('Digite o numero '))
if (n1==0):
    print('O valor eh igual a zero')
elif (n1 > 0):
    print(n1, 'eh positivo')
else:
    print(n1, ' eh negativo')
