#Colocar os numeros em ordem crescente 
import os 
os.system('cls')

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))
n3 = int(input('Número 3: '))

if n1 < n2:
    if n1 < n3:
        primeiro = n1
elif n2 < n3:
    if n2 < n1:
        primeiro = n2
else:
    primeiro = n3

if n1 > n3:
    if n1 > n2:
        maior = n1 
elif n2 > n3:
    if n2 > n1: 
        maior = n2
else:
    maior = n3
segundo = n1 + n2 + n3 - primeiro - maior 

print(f'ordem crescente {primeiro}, {segundo} e {maior}.')