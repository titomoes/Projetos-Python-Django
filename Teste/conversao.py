c = 1
maior = 0
menor = 99999999
while c <= 3:
    aluno_nome = input("Informe o nome do aluno: ")
    aluno_altura = int(input("Informe a altura do aluno: "))

    if aluno_altura > maior:
        maior = aluno_altura
        aluno_mais_alto = aluno_nome
    if aluno_altura < menor:
        menor = aluno_altura
        aluno_mais_baixo = aluno_nome
    c = c + 1

print("O aluno mais alto é %s e mede %5.2f" % (aluno_mais_alto, maior))
print("O aluno mais baixo é %s e mede %5.2f" % (aluno_mais_baixo, menor))
