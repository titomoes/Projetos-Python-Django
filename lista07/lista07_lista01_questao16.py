# Uma floricultura conhecedora de sua clientela gostaria de fazer um algoritmo que
# pudesse controlar sempre um estoque mínimo de determinadas plantas, pois todo dias,
# pela manhã, o dono faz novas aquisições.
#
# Criar um algoritmo que deixe cadastrar 50
# tipos de plantas e nunca deixar o estoque ficar abaixo do ideal. Para cada planta, o
# dono gostaria de cadastrar o nome, o estoque ideal e a quantidade em estoque.
#
# Dessa forma o algoritmo pode calcular a quantidade que o dono da loja precisa comprar no
# próximo dia. Essa quantidade a ser comprada deve ser impressa (quando maior que
# zero) como uma lista para o dono da floricultura.

estoque = []
matriz_requisito = []
linhas = 3
colunas = 50

for i in range(colunas):
    planta = input("Informe no nome, o estoque ideal e a quantidade: Ex.: Flor 50 30 ").split()
    planta_registro = [planta[0], int(planta[1]), int(planta[2])]
    estoque.append(planta_registro)

for n in estoque:
    lista_requisito = []

    if n[1] > n[2]:
        lista_requisito = [n[0], n[1] - n[2]]
        matriz_requisito.append(lista_requisito)

print(matriz_requisito)
