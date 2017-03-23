# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Sabe-se que para iluminar de maneira correta os comodos de uma casa,para cada m²
# deve-se usar 18W de potencia.Faça um programa que receba as duas dimensões de um comodo(em metros)
# (em metros), calcule e mostre a sua area(em m²) e a potencia que sera utilizada
# ----------------------------------------------------------
compri = float(input('Digite a primeira dimensao '))
larg = float(input('Digite a segunda dimensao '))
area = compri * larg
print('A area eh ', area, 'm² e a potencia de iluminacao devera ser utilizada eh ', area * 18, "W")
