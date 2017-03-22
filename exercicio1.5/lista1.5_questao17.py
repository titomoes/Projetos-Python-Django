# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
#Faça um programa que receba o raio,calcule e mostre
#a)o comprimento de uma esfera, sabe-se C=2*pi*R
#b)a area de uma esfera,sabe-se que A= pi*R²
#c)o volume de uma esfera, sabe-se que V=3/4*pi*R³
# ----------------------------------------------------------
import math
r=float(input('Digite um raio '))
print('O comprimento da esfera eh ',2*math.pi*r)
print('A area da esfera eh ',math.pi*r**2)
print('O volume da esfera eh ',(3/4)*math.pi*r**3)