import re

def validaHora(horario):
    vet=(re.findall(r'\d\d',horario))
    if (not vet) or (len(vet) != 3):
        return False
    else:
        srt=r'[0-9]{2}\:?[0-9]{2}\:[0-9]{2}'
        hora=int(vet[0])
        minuto=int(vet[1])
        segundo=int(vet[2])
        flag =True
        if hora>24 or hora<0:
            flag=False
        if minuto>60 or minuto<0:
            flag=False
        if segundo>60 or segundo<0:
            flag=False
        if flag:
            return horario
        else:
            return False


x=input()
print(validaHora(x))
