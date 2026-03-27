numero = int(input('Digite um número: '))

par = numero % 2 == 0

if par:
    print(f'O número {numero} é par')
else:
    print(f'O número {numero} é ímpar')