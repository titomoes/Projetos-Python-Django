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
