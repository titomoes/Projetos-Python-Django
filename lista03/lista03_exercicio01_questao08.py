# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# ----------------------------------------------------------
n1 = float(input('Primeiro produto '))
n2 = float(input('Segundo numero '))
n3 = float(input('Terceiro numero '))
menor = n1;
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print('O melhor preco eh', menor)
