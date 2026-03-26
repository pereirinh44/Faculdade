import os
os.system('cls')

compra = float(input("valor da compra: "))

if compra > 1000:
    desconto = compra * 0.1
    valorDesconto = compra - desconto

elif compra >= 500:
    desconto = compra * 0.05
    valorDesconto = compra - desconto
else:
    desconto = 0
    valorDesconto = compra - desconto
   
print(f'Valor da compra: R$ {compra:.2f}')
print(f'valor do desconto: R$ {desconto:.2f}')
print(f'valor com desconto: R$ {compra:.2f}')