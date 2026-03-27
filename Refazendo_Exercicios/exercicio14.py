num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))
num3 = int(input('Número 3: '))

if num1 >= num2 and num1 >= num3:
    print(f'Maior valor {num1}')
elif num2 >= num1 and num2 >= num3:
    print(f'Maior valor {num2}')
else:
    print(f'Maior valor {num3}')