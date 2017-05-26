# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA
#
# e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente,
#
# valide a data e retorne NULL caso a data seja inválida.

from lista08.ipc import funcoes

data = input("Informe data no formato DD/MM/AAAA: ")

print(funcoes.data_mes_extenso(data))