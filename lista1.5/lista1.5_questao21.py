# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba o numero de horas trabalhadas,o salario minimo
# e o numeor de horas extras trabalhadas. Calcule e mostre o salario a receber
# seguindo as regras a seguir
# a hora trabalhada vale 1/8 do salario minimo
# a hora extra vale vale 1/4 do salario minimo
# o salario bruto equivale ao numero de horas trabalhadas multiplicado pelo valor da hora trabalhada
# a quantia a receber pelas horas trabalhadas equivale ao numero de horas extras trabalhadas multiplicado pelo valor da hora extra
# o salario a receber equivale ao salario bruto mais a quantia a receber pelas horas extras.
# ----------------------------------------------------------
hwork = float(input('Numero de horas trabalhadas '))
salaryminimal = float(input('Salario minimo '))
hextra = float(input('Numero de horas extras'))
valorwork = (1 / 8) * salaryminimal
valorextra = (1 / 4) * salaryminimal
salarybruto = hwork * valorwork
salaryextra = hextra * valorextra
salarytotal = salarybruto + salaryextra
print('O salario total eh ', salarytotal)
