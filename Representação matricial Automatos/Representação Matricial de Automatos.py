import ast
d=input()
n=int(input())
a=ast.literal_eval(d)
estados=a['estados']
inicial=a['inicial']
final =a['final']
delta =a['delta']
x=0

def produto_matriz(matrizA, matrizB):
    matrizR = []
    for i in range(len(matrizA)):
        matrizR.append([])
        for j in range(len(matrizB[0])):
            val = 0
            for k in range(len(matrizA[0])):
                val += matrizA[i][k]*matrizB[k][j]
            matrizR[i].append(val)
    return matrizR

def montapi(estados,inicial):
    pi=cria_matriz_zerada(estados,1)
    for i in range(estados):
        for j in range(1):
            if(i==inicial):
                pi[i][j]=1
    return pi

def montaN(estados,final):
    n=cria_matriz_zerada(estados,1)
    for i in range(len(final)):
        for j in range(estados):
            if(final[i]==j):
                n[j][0]=1
    return n

def cria_matriz_zerada(n, m):
    matriz = []
    for i in range(n):
        linha = m*[0]
        matriz.append(linha)
    return matriz

def montaTransposta(matriz,estados):
    transposta=[]
    for j in range(1):
        transposta.append([])
        for i in range (estados):
            entrada=matriz[i][j]
            transposta[j].append(entrada)
    return transposta

def montaXwa(delta):
    xa=cria_matriz_zerada(estados,estados)
    for i in range(estados):
        for j in range(estados):
            valor =delta[i][0]
            if(valor==j):
                xa[i][j]=1
            else:
                xa[i][j]=0
    return xa

def montaXwb(delta):
    xb=cria_matriz_zerada(estados,estados)
    for i in range(estados):
        for j in range(estados):
            valor=delta[i][1]
            if(valor==j):
                xb[i][j]=1
            else:
                xb[i][j]=0
    return xb

def produto_escalar(matriz, escalar):
    matriz_mult = []
    quant_linhas = len(matriz)
    quant_colunas = len(matriz[0])
    for i in range(quant_linhas):
        matriz_mult.append([])
        for j in range(quant_colunas):
            mult = escalar * matriz[i][j]
            matriz_mult[i].append(mult)
    return matriz_mult

def ordenadelta(delta,estados):
    for i in range(estados):
            delta[i].sort()
    return delta

def refatorasaida(res):
    if (res[0][0]==1):
        print('ACEITA')
    else:
        print('REJEITA')
        
while(x!=n):
    ex=input()
    pi=montapi(estados,inicial)
    deltaok=ordenadelta(delta,estados)
    matriz=montaTransposta(pi,estados)
    res=montaN(estados,final)
    for i in range(len(ex)):
        if(ex[i]=='a'):
            matriz=produto_matriz(matriz,montaXwa(deltaok))
        elif(ex[i]=='b'):
            matriz=produto_matriz(matriz,montaXwb(deltaok))
        else:
            matriz=produto_escalar(matriz,1)
    res=produto_matriz(matriz,res)
    refatorasaida(res)
    x+=1
