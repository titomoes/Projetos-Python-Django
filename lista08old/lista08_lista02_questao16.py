# 16. Faça um procedimento que recebe, por parâmetro,
# 2 vetores de 10 elementos inteiros e que calcule e retorne,
# também por parâmetro, o vetor intersecção dos dois primeiros.


from lista08.ipc import vetor

vetor1 = vetor.cria_vetor(10)
vetor2 = vetor.cria_vetor(10)

vetor_interseccao = vetor.vetor_interseccao(vetor1, vetor2)

print(vetor_interseccao)
