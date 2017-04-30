ages = input().split()
i = 0
acm = 0
cont = 0
for i in range(len(ages)):
    if (int(ages[i]) >= 0):
        cont += +1
        acm += +int(ages[i])
    else:
        break
media = acm / cont
print(media)
