# A gerente do cabeleireiro Sempre Bela tem uma tabela em que registra os “pés” as
# “mãos” e o serviço de podologia das cinco manicures.
#
# Sabendo-se que cada uma ganha 50% do que faturou ao mês,
#
# criar um algoritmo que possa calcular e imprimir
#
# - quanto cada um vai receber, uma vez que não têm carteiras assinadas;
#
# os valores, respectivamente, são R$ 10,00; R$ 15,00 e R$ 30,00.

funcionarios_salarios = []
total_salarios = []

print(float(input()))

qtd = 5

for i in range(qtd):
    salario_registra = []
    salario = input("Informe no nome, a qtd de pés, mãos e serviços de podologia: : Ex.: Maria 50 30 10 ").split()

    salario_registra.append(float(salario[1]) * 10)
    salario_registra.append(float(salario[2]) * 15)
    salario_registra.append(float(salario[3]) * 30)
    print(salario_registra)
    funcionarios_salarios.append(salario)

print(funcionarios_salarios)

for n in funcionarios_salarios:
    salario = []
    salario = [n[0], (n[1] + n[2] + n[3]) * 0.5]
    total_salarios.append(salario)

print(total_salarios)
