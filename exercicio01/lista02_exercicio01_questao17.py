# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
# ----------------------------------------------------------https://github.com/jucimarjr/IPC_2017-1.git
area = float(input('Qual o tamanho em metros quadrados da area a ser pintada? '))
l = area / 6
tot_lit = l - l / 10  # acrescimo da folga

if tot_lit % 18 == 0:
    total_lat = tot_lit / 18
    price_lat = float((total_lat * 80))
elif (tot_lit % 18) % 3.6 == 0:
    total_gal = int((tot_lit % 8) / 3.6) + 1
    price_gal = 25 * total_gal

print(total_lat, price_lat)
print(total_gal, price_gal)
