# Jogo de Craps. Faça um programa de implemente um jogo de Craps.
#
# O jogador lança um par de dados, obtendo um valor entre 2 e 12.
#
# Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
#
# Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu.
#
# Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
#
# Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
#
# Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.


from lista08.ipc import funcoes

cont = 0

while True:

    jogar = int(input("Digite 1 para jogar dados \nDigite zero para sair: "))
    dados = funcoes.jogar_dados()
    print("Dados:", dados)

    if jogar == 1:
        if cont == 0:
            pontos = funcoes.jogar_jogo(dados, cont, 0)
            aux = pontos
        else:
            pontos = funcoes.jogar_jogo(dados, cont, aux)
            aux = pontos

    print("Pontos:", aux)

    cont += 1
