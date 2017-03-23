# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual,calcule e mostre:
# a)a idade dessa pessoa em anos;
# b)a idade dessa pessoa em meses;
# c)a idade dessa pessoa em dias;
# d)a idade dessa pessaos em semanas;
# ----------------------------------------------------------
dborn=int(input('Data de nascimento'))
dnow=int(input('Data atual '))
print('idade em anos ',dnow-dborn)
print('idade em meses',(dnow-dborn)*12)
print('idade em dias ',(dnow-dborn)*365)
print('idade em semanas ',(dnow-dborn)*52)
