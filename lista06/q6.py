# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.
# ----------------------------------------------------------
list_media = []
list_notas = []
cont = 0
for i in range(3):
    media = 0
    list_notas = []
    print('Aluno: ', i + 1)
    for j in range(4):
        list_notas.append(float(input()))
        media += list_notas[j]
    media = media / 4
    list_media.append(media)
    if list_media[i] >= 7:
        cont += 1
print(cont)
