total=0
cont=0

while True:
    n=float(input('Produto'))
    if n!=0:
        total=total+n
        cont=cont+1
    else:
        print('Produto ',cont,': ',n)
        print('Total: ',total)
        din=float(input('Dinheiro :'))
        print('Troco: ',din-total)
        break
