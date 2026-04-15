n1 = int(input('Entrada: '))
n2 = int(input('Entrada: '))

ordem = input('C para Crescente e D para descente: ').lower()
if ordem == 'c' or ordem == 'd':
    print('Saida: ', end = ' ')
    if ordem == 'c':
        if n1 <= n2:
            for i in range(n1, n2+1, 1):
                print(i, end = ' ')
        else:
            for i in range(n2, n1+1, 1):
                print(i, end = ' ')
    else:
        if n1 <= n2:
            for i in range(n2,n1-1, -1):
                print(i, end = ' ')
        else:
            for i in range(n1, n2-1, -1):
                print(i, end = ' ')
else:
    print('Digite novamente C ou D')
