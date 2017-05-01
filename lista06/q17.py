# ----------------------------------------------------------
# Introdução a Programação de Computadores - IPC
# Universidade do Estado do Amazonas - UEA
# Prof. Jucimar Jr
# Vitor Simoes Azevedo	    1715310025
# nome completo do aluno 2	matrícula do aluno 2
# nome completo do aluno 3	matrícula do aluno 3
# nome completo do aluno 4	matrícula do aluno 4
#
# Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
# O resultado do atleta será determinado pela média dos cinco valores restantes.
#  Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
#  os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
#  A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo
#
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m
#
# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
list_saltos = []
nome =[]
media = 0


# while True:
#     nome = str(input('Atleta: \b'))
#     if (nome != ""):
#         for i in range(5):
#             list_saltos.append(float(input(str(i + 1) + ' Salto: \b')))
#             media += list_saltos[i]
#     else:
#         media = media / 5
#         print('Resultado Final:')
#         for j in range(len(nome)):
#             print('Atleta: ' + nome )
#             print('Saltos: ' + str(list_saltos[j]) + ' - ' + str(list_saltos[j + 1]) + ' - ' + str(list_saltos[j + 2]) + ' - ' + str(list_saltos[j + 3]))
#             print('Média dos Saltos: ' + str(media) + ' m')
#