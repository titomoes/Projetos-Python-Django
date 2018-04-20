import re

def validaano(ano):
    srt=r'[0-9]{4}\/?[0-9]{2}\/[0-9]{2}'
    vet=re.findall(r'\d\d',ano)
    # vet2=re.findall(r'\d\d',vet)
    if (not vet) or (len(vet) != 4):
        return False
    else:
        mano=int(vet[0]+vet[1])
        mes=int(vet[2])
        dia=int(vet[3])
        flag= True
        cont=0
        while flag and cont==0:
            if mano%4 == 0 and mano%100!= 0 or mano%400 == 0:
                bix = True
            else:
                bix = False
            if 12<mes<1:
                flag = False
            if dia > 31 or ((mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30):
                flag = False
            if (mes == 2 and bix == False and dia > 28) or ( mes == 2 and bix == True and dia > 29):
                flag = False
            cont+=1
        if flag:
            return ano
        else:
            return False

x=input()
print(validaano(x))
