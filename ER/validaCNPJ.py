import re

def validacnjp(cnpj):
    vet=(re.findall('\d',cnpj))
    if (not cnpj) or (len(vet) < 14):
        return False
    else:
        srt=r'([0-9]{2}\.?[0-9]{3}\.?[0-9]{3}\/?[0-9]{4}\-?[0-9]{2})'
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

x=input()
print(validacnjp(x))
