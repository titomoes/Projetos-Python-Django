# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um Programa que leia três números e mostre-os em ordem decrescente.
# ----------------------------------------------------------
n1 = int(input('Primeiro numero '))
n2 = int(input('Segundo numero '))
n3 = int(input('Terceiro numero '))
if n1 > n2 and n1 > n3 and n2 > n3:
    print(n1, n2, n3)
elif n1 > n2 and n1 > n3 and n3 > n2:
    print(n1, n3, n2)
elif n2 > n1 and n2 > n3 and n1 > n3:
    print(n2, n1, n3)
elif n2 > n1 and n2 > n3 and n3 > n1:
    print(n2, n3, n1)
elif n3 > n1 and n3 > n2 and n1 > n2:
    print(n3, n1, n2)
elif n3 > n1 and n3 > n1 and n2 > n1:
    print(n3, n2, n1)
