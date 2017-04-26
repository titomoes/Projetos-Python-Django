notas = input().split()
i = 0
acm = 0
cont = 0
for i in range(len(notas)):
    if (float(notas[i]) >= 0 and float(notas[i]) <= 10):
        acm += +float(notas[i])
        cont += +1
    else:
        print("nota invalida")
media = round(acm / cont,2)
print(media)
