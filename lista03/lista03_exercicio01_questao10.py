# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# FFaça um Programa que pergunte em que turno você estuda.
#  Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# ----------------------------------------------------------
turn=input('qual turno voce estuda?')
if turn=='M':
    print('Bom dia')
elif turn=='V':
    print('Boa tarde')
elif turn=='N':
    print('Boa noite')
else:
    print('valor invalido')
