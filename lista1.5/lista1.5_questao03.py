# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba dois numeros, calcule e mostre a divisao do primeiro pelo segundo
# Sabe-se que o segundo numero não pode ser 0, portanto não é necessário se preocupar com validaçoes
# ----------------------------------------------------------
n1 = float(input('Digite n1'))
n2 = float(input('Digite n2'))
if (n2 == 0):
    print('Não existe divisão por zero')
else:
    print('A divisão eh', n1 / n2)
