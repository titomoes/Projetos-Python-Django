# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
# ----------------------------------------------------------
n1=int(input('Digite o primeiro numero inteiro: '))
n2=int(input('Digite o segundo numero inteiro '))
n3=float(input('Digite o terceiro numero inteiro '))
print('O produto do dobro do primeiro com metade do segundo eh: ',(2*n1)*(n2/2))
print('A soma do triplo do primeiro com o terceiro eh: ',3*n1+n3)
print('O terceiro elevado ao cubo eh: ',n3**3)