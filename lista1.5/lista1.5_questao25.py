# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba uma hora(uma hora variavel para hora e outra para minutos)
# e mostre:
# a) a hora digitada convertida em minutos
# b)total em minutos,ou seja, os minutos digitados mais a conversao anterior
# c)total de minutos convertidos em segundos
# ----------------------------------------------------------
hours = float(input('Digite a hora'))
minutes = float(input('Digite os minutos'))
totalminutes = hours * 60 + minutes
print('hora convertida em minutos eh ', hours * 60)
print('Minutos total ',totalminutes )
print('Minutos total convertido em segundos ',totalminutes*60)
