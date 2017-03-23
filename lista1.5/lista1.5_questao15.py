# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Joao recebeu seu salario e precisa pagar duas contas que estao atrasadas
# Como as contas estão atrasadas, Joao terá  de pagar multa de 2% sobre cada conta,
# Faça um programa que calcule e mostre quanto restará do salario do João
# ----------------------------------------------------------
salary=float(input("Qual seu salario Joao?"))
cont1=float(input('Primeira conta a pagar '))
cont2=float(input('Segunda conta a pagar  '))
print('O restante do salario pagando as multas',salary-(cont1+cont1*0.02)-(cont2+cont2*0.02))