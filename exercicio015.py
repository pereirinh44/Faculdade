#número intermediario 

import os 
os.system('cls')

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if n1 > n2:
    if n1 < n3:
        print(f'Valor intermediário {n1}.')
    elif n1 > n3:
        if n1 < n2:    
         print(f'Valor intermediário {n1}.')


elif n2 > n1:
    if n2 < n3:
        print(f'Valor intermediário {n2}.')
elif n2 > n3:
    if n2 < n1:
        print(f'Valor intermediário {n2}.')



elif n3 > n2:
    if n3 < n1:
        print(f'Valor intermediário {n3}.')
elif n3 > n1:
    if n3 < n2:
        print(f'Valor intermediário {n3}.')
