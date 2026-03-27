num1 = int(input('Compra: '))
num2 = int(input('''PIX: 1
dinheiro: 2
Débito: 3
Credito: 4
Qual a forma de pagamento: '''))


pix = num1 * 0.95
dinheiro = num1
debito = num1 * 1.01
credito = num1 * 1.05

if num2 == 1:
    print(f'valor original: R$ {num1}')
    print(f'valor ajustado: R$ {pix}')
elif num2 == 2:
    print(f'valor original: R$ {num1}')
    print(f'valor ajustado: R$ {dinheiro}')
elif num2 == 3:
    print(f'valor original: R$ {num1}')
    print(f'valor ajustado: R$ {debito}')
elif num2 == 4:
    print(f'valor original: R$ {num1}')
    print(f'valor ajustado: R$ {credito}')
