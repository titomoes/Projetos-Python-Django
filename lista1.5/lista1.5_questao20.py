# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um programa que receba a medida do angulo formado por uma escada apoiada no chao
# e a distancia que a escada esta da parede.Calcule e mostre a medida da escada para que se
# se possa alcançar a ponta da escada
# ----------------------------------------------------------
#usar angulo em rad
import math

angular = float(input('Digite o angulo'))
dx = float(input('Digite a distancia da escada até a parede'))
hipo = dx / math.cos(angular)
print('a medida da escada para que se possa alcançar a ponta da escada eh ', hipo)
