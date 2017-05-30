# 20. Faça um procedimento que receba, por parâmetro, um vetor K(15) e retorna,
# também por parâmetro, um vetor P contendo apenas os valores primos de K.

from lista08.ipc import vetor

vetor1 = vetor.cria_vetor(15)

print(vetor1)

p = vetor.vetor_de_primos(vetor1)

print(p)