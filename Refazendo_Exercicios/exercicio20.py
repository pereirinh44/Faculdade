sal = float(input('Salário: '))

if sal <= 2259.20:
    ir = 0
    print(f'Salário R$ {sal}')
    print(f'IR R$ {ir}')

elif sal > 2259.20 and sal <= 2826.65:
    ir = sal * 0.075 - 169.44
    print(f'Salário R$ {sal}')
    print(f'IR R$ {ir}')

elif sal > 2826.65 and sal <= 3751.05:
    ir = sal * 0.15 - 381.44
    print(f'Salário R$ {sal}')
    print(f'IR R$ {ir}')

elif sal > 3751.05 and sal <= 4664.68:
    ir = sal * 0.225 - 662.77
    print(f'Salário R$ {sal}')
    print(f'IR R$ {ir}')

else:
    ir = sal * 0.275 - 896.00
    print(f'Salário R$ {sal}')
    print(f'IR R$ {ir}')