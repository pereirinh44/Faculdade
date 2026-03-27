sal = float(input('Sálario: '))

if sal <= 1518:
    inss = sal * 0.075
    print(f'Salário {sal}')
    print(f'INSS R$ {inss}')
elif sal >1518 and sal <= 2793.88:
    inss = sal * 0.09 -22.77
    print(f'Salário {sal}')
    print(f'INSS R$ {inss}')
elif sal > 2793.88 and sal <= 4190.83:
    inss = sal * 0.12 - 106.59
    print(f'Salário {sal}')
    print(f'INSS R$ {inss}')
elif sal > 4190.83 and sal <= 8157.41:
    inss = sal * 0.14 - 190.40
    print(f'Salário {sal}')
    print(f'INSS R$ {inss}')
else:
    teto = 8157.41
    inss = teto * 0.14 - 190.40
    print(f'Salário {sal}')
    print(f'INSS R$ {inss}')