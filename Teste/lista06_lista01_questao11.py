vetores = []
vetor4 = []
n = 0

while n < 3:
    vet = []
    m = 0
    while m < 2:
        numero = int(input())
        vet.append(numero)
        m += 1
    vetores.append(vet)
    n += 1
i=0
print (vetores)
for i in vetores:
    vetor4[i]=vetores.insert(i,3)
print (vetor4)