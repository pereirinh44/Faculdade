salario_fixo = float(input('Digite o valor do seu salário fixo: '))
venda_mes = int(input('qual foi sua venda no mês: '))

if venda_mes > 100000:
    print(f'Bônus de R$ {salario_fixo * 2:.2f}')
else: 
    print(f'Bônus de R$ {salario_fixo * 1.5:.2f}')