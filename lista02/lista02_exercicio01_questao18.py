# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
# ----------------------------------------------------------
mb = float(input('Tamanho do arquivo '))
mbps = float(input('Velocidade do link de Internet '))
time = mb / mbps
minute = time / 60
print('O tempo aproximado para download do arquivo atraves desse link eh', minute)
