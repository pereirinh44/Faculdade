compra = float(input('digite o valor da compra: '))

if compra > 5000:
    desconto = compra * 0.075
    print(f'Valor original R${compra:.2f}')
    print(f'Com desconto R${compra - desconto:.2f}')
else: 
    desconto = compra * 0.035
    print(f'Valor original R${compra:.2f}')
    print(f'Com desconto R$ {compra - desconto:.2f}')