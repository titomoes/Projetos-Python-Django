Representação Matricial de AFD's
=================================

Apresetação A computação de um autômato finito determinístico A = hQ, Σ, δ, q0, Fi pode ser representada segundo uma notação matricial, descrita como segue:

1. Deve-se ordenar os estados do autômato;
2. Construir o vetor-coluna π, identificando o estado inicial do autômato. O elemento correspondente ao estado inicial deve possuir o valor 1, e os demais elementos devem ser nulos;
3. Construir o vetor-coluna η, identificando os estados de aceitação do autômato. Os elementos que denotem estados de aceitação devem ser iguais a 1 e os demais iguais a 0;
4. Para cada símbolo a ∈ Σ, definir a matriz de transição Xa, na qual as linhas e colunas correspondem aos estados do autômato. A entrada para a linha correspondente ao estado qi, e para a coluna correspondente ao estado qj é igual a 1 se δ(qi, a) = qj, e 0 em caso contrário.
5. Para verificar se ω ∈ L(A), basta utilizar a seguinte expressão:

πˆT*Xω*η ={
1, se ω ∈ L(A)
0, caso contrário,
}

em que Xω é a matriz resultante da multiplicação das matrizes correspondentes a os símbolos da palavra ω.
