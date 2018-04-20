import re

def validaCodigo(codigo):
    str=r'\d{9}-\w{6}-\d*[02468]-[0-1]{3}'
    vet=''.join(re.findall(str,codigo))
    if (not vet) or (len(vet) <0):
        return False
    else:
        return codigo

x=input()
print(validaCodigo(x))
