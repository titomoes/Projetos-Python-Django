# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Um funcionario recebe um salario fixo mais 4% de comissao sobre vendas.
# Faça um programa que recebao salario fixo de um funcionario e o valor de
# suas vendas,calcule e mostre a comissão e o salario final do funcionario
# ----------------------------------------------------------
salary = float(input('Digite o salario '))
sales = float(input('Digite o valor de vendas '))
print('Sua comissao eh ',0.04*sales,'e salario total eh ',salary+0.04*sales)
