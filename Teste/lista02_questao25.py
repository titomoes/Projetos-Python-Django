n=0
maior=0
menor=9999
while n<3:
    num=int(input('numero'))
    if num>maior:
        maior=num
    if num<menor:
        menor=num
    n += 1
print(maior,menor)

inicio
    inteiro maior,menor,cont
    enquanto cont<3 faca
        escrever('Digite o numero')
        ler(num)
        se (num>maior) faca
            maior=num
        fimse
        se (num<menor) faca
            menor=num
        fimse
        cont <- cont+1
    fimenquanto
    escrever('O maior eh ',maior,'e o Menor eh ',menor)
fim