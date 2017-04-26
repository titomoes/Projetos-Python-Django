num=input().split()
i=1
menor=int(num[i])
for x in range(len(num)):
    if int(num[i])<menor:
        menor= int(num[i])
print(menor)