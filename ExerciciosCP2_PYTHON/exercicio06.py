n1 = int(input('Entrada: '))
n2 = int(input('Entrada: '))

print('Saida: ', end = ' ')

if n1 <= n2:
    for i in range(n1, n2+1, 1):
        print (i, end = ' ')
else:
    for i in range(n2, n1+1, 1):
        print (i, end = ' ')    


