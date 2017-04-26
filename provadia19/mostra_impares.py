num = input().split()
num_menor = int(num[0])
num_maior = int(num[1])
while num_menor <= num_maior:
    if (num_menor % 2 != 0):
        print(num_menor)
    num_menor += 1
