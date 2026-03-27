salario = float(input('Digite seu salário: '))

if salario <= 1518:
    inss = salario * 0.075
    print(f'INSS R$ {inss:.2f}')
elif 1518.01 <= salario <= 2793.88:
    inss = salario * 0.09 - 22.77
    print(f'INSS R$ {inss:.2f}')
elif 2793.89 <= salario <= 4190.83:
    inss = salario * 0.12 - 106.59
    print(f'INSS R$ {inss:.2f}')
elif 4190.84 <= salario <= 8157.41:
    inss = salario * 0.14 - 190.40
    print(f'INSS R$ {inss:.2f}')
else:
    inssFixo = 8157.41 * 0.14 - 190.40
    print(f'INSS R$ {inssFixo:.2f}')