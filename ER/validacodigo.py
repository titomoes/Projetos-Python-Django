import re
cpf=""
cnpj=""
data=""
hora=""
preco=""
a=input()
cpf = ''.join(re.findall('\d{3}\.\d{3}\.\d{3}-\d{2}', a))
cnpj= ''.join(re.findall('\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}',a))
data= ''.join(re.findall('\d{4}\.\d{2}\.\d{2}',a))
hora= ''.join(re.findall('\d{2}\:\d{2}\:\d{2}',a))
preco= ''.join(re.findall('\[\d+\.\d{2}[\,]?\d+\.\d{2}\]',a))
# codigo= ''.join(re.findall('\d{9}-\w{6}-\d*[02468]-[0-1]{3}',a))

def validacpf(cpf):
    vet=(re.findall(r'\d',cpf))
    if (not vet) or (len(vet) < 11):
        return False
    else:
        marc=[10, 9, 8, 7, 6, 5, 4, 3, 2]
        newvet=vet[:9]
        while len(newvet) < 11:
            acm=0
            r=0
            for i in range(len(newvet)):
                acm+=int(newvet[i])*marc[i]
            r=acm%11
            if r>1:
                v=11-r
            else:
                v=0
            newvet.append(str(v))
            marc.insert(0,11)
        if newvet == vet:
            return cpf
        else:
            return False

def validacnjp(cnpj):
    vet=(re.findall('\d',cnpj))
    if (not cnpj) or (len(vet) < 14):
        return validacpf(cnpj)
    else:
        marc=[5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        newvet=vet[:12]
        while len(newvet) < 14:
            acm=0
            r=0
            for i in range(len(newvet)):
                acm+=int(vet[i])*marc[i]
            r=acm%11
            if r>1:
                v=11-r
            else:
                v=0
            newvet.append(str(v))
            marc.insert(0,6)
        if newvet == vet:
            return cnpj
        else:
            return False

def validaano(ano):
    vet=re.findall(r'\d\d',ano)
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

def validaHora(horario):
    vet=(re.findall(r'\d\d',horario))
    if (not vet) or (len(vet) != 3):
        return False
    else:
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

def validaPreco(preco):
    if (not preco) or (len(preco) <0):
        return False
    else:
        return preco

# def validaCodigo(codigo):
#     if (not codigo) or (len(codigo) <0):
#         return False
#     else:
#         return codigo

flag1=validacpf(cpf)
flag2=validacnjp(cnpj)
flag3=validaano(data)
flag4=validaHora(hora)
flag5=validaPreco(preco)
# flag6=validaCodigo(codigo)

if flag1 and flag2 and flag3 and flag4 and flag5:
    print(True)
else:
    print(False)
