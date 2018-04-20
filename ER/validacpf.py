import re

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

x=input()
print(validacpf(x))

159.200.335-41 159.200.335-41 2018.03.12 23:45:12 [3.15,99.65]
