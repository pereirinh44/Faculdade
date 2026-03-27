num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

if num1 <= num3 and num1 <= num2:
    menor = num1
elif num2 <= num3 and num2 <= num1:
    menor = num2
else:
    menor = num3
if num1 >= num2 and num1 >= num3:
    maior = num1 
elif num2 >= num1 and num2 >= num3:
    maior = num2
else:
    maior = num3

intermediario = num1 + num2 + num3 - menor - maior

print(f'Ordem crescente {menor}, {intermediario} e {maior}')