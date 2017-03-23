# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba o valor dos catetos de um triangulo,calcule e mostre o valor da hipotenusa.
# ----------------------------------------------------------
from math import sqrt

c = int(input("Digite o primeiro cateto "))
b = int(input("Digite o segundo cateto "))
a = sqrt(c ** 2 + b ** 2)
print('A hipotenusa eh ', a)
