# 19. Faça um procedimento que recebe, por parâmetro,
# 2 vetores de 15 elementos inteiros e que calcule e retorne,
# também por parâmetro, o vetor produto dos dois primeiros.


from lista08.ipc import vetor

vetor1 = vetor.cria_vetor(10)
vetor2 = vetor.cria_vetor(10)

vetor = vetor.vetor_produto(vetor1, vetor2)

print(vetor)
