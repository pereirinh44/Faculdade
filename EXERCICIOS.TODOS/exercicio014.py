n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if n1 > n2:
    if n1 > n3:
        print(f'Maior valor {n1}.')
elif n2 > n3:
    print(f'Maior valor {n2}.')
else:
    print(f'Maior valor {n3}.')