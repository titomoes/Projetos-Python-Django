# 21. Faça um procedimento que receba um vetor A(100) de inteiros
# e retorna esse mesmo vetor compactado, ou seja,
# sem os seus valores nulos(zero) e negativos.


from lista08.ipc import vetor

vetor1 = vetor.cria_vetor(100)


vetor_compactado = vetor.vetor_compactado(vetor1)

print(vetor_compactado)


