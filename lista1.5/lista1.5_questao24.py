# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba a quantidade de dinheiro em reais que uma pessoa que vai viajar possui
# Essa pessoa vai passar por varios paises e precisa converter seu dinheiro em dolar,marco alemao e
# e libra esterlina. Sabe-se que a cotação do dolar é de R$ 1,80, do marco alemao R$2,00 e da libra
# esterlina é R$1,57. O programa deve fazer as conversões e mostra-las
# ----------------------------------------------------------
money=float(input('Digite seu dinheiro em reais '))
print('Seu dinheiro em dolar eh ',money*1.80)
print('Seu dinheiro em marco alemao eh ',money*2)
print('Seu dinheiro em libra esterlina eh ',money*1.57)