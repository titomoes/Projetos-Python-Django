# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um Programa que leia três números e mostre o maior e o menor deles.
# ----------------------------------------------------------
n1 = int(input('Primeiro numero '))
n2 = int(input('Segundo numero '))
n3 = int(input('Terceiro numero '))
maior = n1;
menor = n1;
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3
print(maior, 'e', menor)
