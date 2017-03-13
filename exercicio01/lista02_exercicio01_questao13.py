# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7 (h = altura)
# Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
# ----------------------------------------------------------
h = float(input('Digite sua altura: '))
s = input('Digite seu sexo ')
if s == 'm':
    p = float(input('Digite seu peso: '))
    if p == (72.7 * h) - 58:
        print('Seu peso esta ideal')
    elif p < (72.7 * h) - 58:
        print('Seu peso esta abaixo do padrao')
    else:
        print('Seu peso esta acima do padrao')
elif s == 'f':
    p = float(input('Digite seu peso: '))
    if p == (62.1 * h) - 44.7:
        print('Seu peso esta ideal')
    elif p < (62.1 * h) - 44.7:
        print('Seu peso esta abaixo do padrao')
    else:
        print('Seu peso esta acima do padrao')
