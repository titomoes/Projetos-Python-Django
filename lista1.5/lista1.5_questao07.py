# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba o peso de uma pessoa,calcule e mostre:
#a)novo peso se a pessoa engordar 15%sobre o peso digitado
#b)novo peso se a pessoa emagrecer 20% sobre o peso digitado
# ----------------------------------------------------------
weight = float(input('Digite o peso '))
print("novo peso se a pessoa engordar ",weight+weight*0.15)
print("novo peso se a pessoa emagrecer ",weight-weight*0.2)
