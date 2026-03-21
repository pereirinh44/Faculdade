import os 
os.system('cls')

compra = float(input('Valor da compra: '))

pix = compra - (compra * 0.05)
debito = compra + (compra * 0.01)
credito = compra + (compra * 0.025)

print("""Formas de pagamento
PIX - 1
dinheiro - 2
Débito - 3
Crédito - 4     """)
forma_pagamento = int(input('Escolha a forma de pagamento: '))

if forma_pagamento == 1:
    print(f'Valor original R$ {compra:.2f}')
    print(f'Valor ajustado R$ {pix:.2f}')
elif forma_pagamento == 4:
    print(f'Valor original R$ {compra:.2f}')
    print(f'Valor ajustado R$ {credito:.2f}')
elif forma_pagamento == 3:
    print(f'Valor original R$ {compra:.2f}')
    print(f'Valor ajustado R$ {debito:.2f}')
elif forma_pagamento == 2:
    print(f'Valor original R$ {compra:.2f}, sem ajustes para dinheiro!')
    






