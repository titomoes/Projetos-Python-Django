# 23. Uma locadora de vídeos tem guardada, em um vetor A de 500 posições,
# a quantidade de filmes retirados por seus clientes durante o ano de 1997.
# Agora, esta locadora está fazendo uma promoção e, para cada 15 filmes retirados,
# o cliente tem direito a uma locação grátis.
# Faça um procedimento que receba o vetor A por parâmetro e retorna,
# também por parâmetro, um vetor contendo a quantidade de locações
# gratuitas a que cada cliente tem direito.


from lista08.ipc import vetor




vetorA = vetor.cria_registro_locadora(500)

vetor_gratuita = vetor.quantidade_gratuita(vetorA)

print(vetorA)
print(vetor_gratuita)


