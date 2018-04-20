import re

def validaPreco(preco):
    vet=""
    str=r'\[\d+\.\d{2}[\,]?\d+\.\d{2}\]'
    vet=''.join((re.findall(str,preco)))
    if (not vet) or (len(vet) <0):
        return False
    else:
        return True

x=input()
print(validaPreco(x))
